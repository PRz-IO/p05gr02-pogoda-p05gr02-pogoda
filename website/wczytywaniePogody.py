from .models import User
from .models import Kraj
from .models import Miasto
from .models import Atrybut
from .models import Jednostka
from .models import stanpogody
from .models import PogodaDzienna
from .models import PogodaGodzinowa
from datetime import datetime, timedelta
from sqlalchemy import delete
import json
import urllib.request

api = '245522d6093c5c70530b541f6a01a0cd'

def wczytaj(app, db):
    # m = urllib.parse.quote('Rzeszów') #zamienia znaki specjalne na kodowane procentowo 
    
    # source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + m + '&appid=' + api).read()
    # dane = json.loads(source)
    # #print(str(dane['coord']['lat']) + ' '+ str(dane['coord']['lon']))
    # lat = str(dane['coord']['lat'])
    # lon = str(dane['coord']['lon'])

    #!!! onecallapi wymaga koordynatów zamiast nazwy miasta, więc najpierw można sczytać koordy dla danego miasta kodem powyżej
    #!!! ewentualnie można dodać do bazy koordynaty czy coś
    #!!! zrobiłem tak bo onecallapi wysyła w jednym odwołaniu pogodę godzinową na 48h i pogodę dzienną na tydzień, a to wyżej tylko aktualną (ale ma te geokodowanie fajne, a onecallapi nie ma)
    
    # source = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/onecall?lat='+lat+'&lon='+lon+'&units=metric&appid=' + api).read()
    # dane = json.loads(source)
    # f = open('website\onecall.json')
    # dane = json.load(f)
    
    with app.app_context():
        #miasta = db.session.query(Miasto).filter_by(id_kraju = 4).all()
        miasta = db.session.query(Miasto).all()
        for miasto in miasta:
            print(miasto.nazwa_miasta)
            m = urllib.parse.quote(miasto.nazwa_miasta)
            source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + m + '&appid=' + api).read()
            dane = json.loads(source)
            lat = str(dane['coord']['lat'])
            lon = str(dane['coord']['lon'])
            source = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/onecall?lat='+lat+'&lon='+lon+'&units=metric&appid=' + api).read()
            dane = json.loads(source)

            for i in dane['daily']:
                dzien = datetime.utcfromtimestamp(i['dt']).date()
                stare = db.session.query(PogodaDzienna).filter(PogodaDzienna.data.between(dzien, dzien+timedelta(hours=24)),PogodaDzienna.id_miasta == miasto.id).first()
                if(stare):
                    db.session.delete(stare)
                if(i['weather'][0]['main'] == 'Clear'):
                    stan = 1
                if(i['weather'][0]['main'] == 'Rain'):
                    stan = 2
                if(i['weather'][0]['main'] == 'Thunderstorm'):
                    stan = 3
                if(i['weather'][0]['main'] == 'Snow'):
                    stan = 4
                if(i['weather'][0]['id'] > 700 and i['weather'][0]['id'] < 800):
                    stan = 5
                if(i['weather'][0]['main'] == 'Clouds'):
                    stan = 6
                if(i['weather'][0]['main'] == 'Drizzle'):
                    stan = 7
                nowaPogodaDzienna = PogodaDzienna(data = datetime.utcfromtimestamp(i['dt']).date(),min_temp = i['temp']['min'],max_temp = i['temp']['max'],rano = i['temp']['morn'],poludnie = i['temp']['day'],wieczor = i['temp']['eve'],noc = i['temp']['night'],opad = i['pop'], miasto = miasto, id_stan_pogody=stan)

            for i in dane['hourly']:
                if(datetime.utcfromtimestamp(i['dt'])>(datetime.today().replace(hour=23,minute=59,second=0) - timedelta(days=1)) and datetime.utcfromtimestamp(i['dt'])<datetime.today().replace(hour=23,minute=59)):
                    stare = db.session.query(PogodaGodzinowa).filter(PogodaGodzinowa.data.between(datetime.today().replace(hour=0,minute=0), datetime.today().replace(hour=23,minute=59)),PogodaGodzinowa.id_miasta == miasto.id).first()
                    #print(stare)
                    #if(stare):
                    #    db.session.delete(stare)
                    if(i['weather'][0]['main'] == 'Clear'):
                        stan = 1
                    if(i['weather'][0]['main'] == 'Rain'):
                        stan = 2
                    if(i['weather'][0]['main'] == 'Thunderstorm'):
                        stan = 3
                    if(i['weather'][0]['main'] == 'Snow'):
                        stan = 4
                    if(i['weather'][0]['id'] > 700 and i['weather'][0]['id'] < 800):
                        stan = 5
                    if(i['weather'][0]['main'] == 'Clouds'):
                        stan = 6
                    if(i['weather'][0]['main'] == 'Drizzle'):
                        stan = 7
                    nowaPogodaGodzinowa = PogodaGodzinowa(data = datetime.utcfromtimestamp(i['dt']), temperatura = i['temp'], predkosc_wiatru = i['wind_speed'], cisnienie = i['pressure'], miasto = miasto, id_stan_pogody = stan)
        db.session.commit()