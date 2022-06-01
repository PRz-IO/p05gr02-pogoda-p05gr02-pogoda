from .models import User
from .models import Kraj
from .models import Miasto
from .models import Atrybut
from .models import Jednostka
from .models import stanpogody
from .models import PogodaDzienna
from .models import PogodaGodzinowa
from datetime import datetime

import json
import urllib.request

api = '245522d6093c5c70530b541f6a01a0cd'

def dodaj(app,db):
    with app.app_context():
        # marek = db.session.query(User).filter_by(username="marek").first()
        # agata = db.session.query(User).filter_by(username="agata").first()
        rzeszow = db.session.query(Miasto).filter_by(nazwa_miasta="Rzeszów").first()
        # rzeszow.uzytkownicy.extend([marek, agata])

        # nU4 = User(email = "167834@stud.prz.edu.pl", username = "ania", password = "haslo123")
        # nU5 = User(email = "164189@stud.prz.edu.pl", username = "milena", password = "haslo123")
        # db.session.add_all([nU4, nU5])

        # rzeszow.uzytkownicy.extend([nU4, nU5])

        # dtemp = db.session.query(Jednostka).filter_by(nazwa_jednostki="C").first()
        # dcis = db.session.query(Jednostka).filter_by(nazwa_jednostki="hPa").first()
        # dpred = db.session.query(Jednostka).filter_by(nazwa_jednostki="km/h").first()
        # dwil = db.session.query(Jednostka).filter_by(nazwa_jednostki="%").first()

        # uzytkownicy_bez_jednostek = db.session.query(User).filter_by(preferencje=None).all()
        # #print(uzytkownicy_bez_jednostek)
        # for uzytkownik in uzytkownicy_bez_jednostek:
        #     print(uzytkownik.username)
        #     uzytkownik.preferencje.extend([dtemp, dcis, dpred, dwil])

        # #db.session.commit()

def zaladuj_przyklad(app, db):
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
    f = open('website\onecall.json')
    dane = json.load(f)
    
    with app.app_context():
        nowyKraj1 = Kraj(nazwa_kraju = "Polska")
        nK2 = Kraj(nazwa_kraju = "Niemcy")
        nK3 = Kraj(nazwa_kraju = "Austria")
        nK4 = Kraj(nazwa_kraju = "Ukraina")
        nK5 = Kraj(nazwa_kraju = "Słowacja")
        nK6 = Kraj(nazwa_kraju = "Litwa")
        nK7 = Kraj(nazwa_kraju = "Czechy")
        nK8 = Kraj(nazwa_kraju = "Białoruś")
        db.session.add_all([nowyKraj1, nK2,nK3,nK4,nK5,nK6,nK7,nK8])
        #db.session.commit()


        polska = db.session.query(Kraj).filter_by(nazwa_kraju='Polska').first()
        niemcy = db.session.query(Kraj).filter_by(nazwa_kraju="Niemcy").first()
        austria = db.session.query(Kraj).filter_by(nazwa_kraju="Austria").first()
        ukraina = db.session.query(Kraj).filter_by(nazwa_kraju="Ukraina").first()
        słowacja = db.session.query(Kraj).filter_by(nazwa_kraju="Słowacja").first()
        litwa = db.session.query(Kraj).filter_by(nazwa_kraju="Litwa").first()
        czechy = db.session.query(Kraj).filter_by(nazwa_kraju="Czechy").first()
        białoruś = db.session.query(Kraj).filter_by(nazwa_kraju="Białoruś").first()

        noweMiasto1 = Miasto(nazwa_miasta = "Rzeszów", kraj = polska)
        nM2 = Miasto(nazwa_miasta = "Warszawa", kraj = polska)
        nM3 = Miasto(nazwa_miasta = "Łódź", kraj = polska)
        nM4 = Miasto(nazwa_miasta = "Wrocław", kraj = polska)
        nM5 = Miasto(nazwa_miasta = "Poznań", kraj = polska)
        nM6 = Miasto(nazwa_miasta = "Gdańsk", kraj = polska)
        nM7 = Miasto(nazwa_miasta = "Szczecin", kraj = polska)
        nM8 = Miasto(nazwa_miasta = "Bydgoszcz", kraj = polska)
        nM11 = Miasto(nazwa_miasta = "Berlin", kraj = niemcy)
        nM12 = Miasto(nazwa_miasta = "Hamburg", kraj = niemcy)
        nM13 = Miasto(nazwa_miasta = "Munich", kraj = niemcy)
        nM14 = Miasto(nazwa_miasta = "Frankfurt", kraj = niemcy)
        nM21 = Miasto(nazwa_miasta = "Wiedeń", kraj = austria)
        nM22 = Miasto(nazwa_miasta = "Graz", kraj = austria)
        nM23 = Miasto(nazwa_miasta = "Linz", kraj = austria)
        nM24 = Miasto(nazwa_miasta = "Salzburg", kraj = austria)
        nM31 = Miasto(nazwa_miasta = "Kijów", kraj = ukraina)
        nM32 = Miasto(nazwa_miasta = "Charków", kraj = ukraina)
        nM33 = Miasto(nazwa_miasta = "Odessa", kraj = ukraina)
        nM34 = Miasto(nazwa_miasta = "Dniepr", kraj = ukraina)
        nM41 = Miasto(nazwa_miasta = "Bratysława", kraj = słowacja)
        nM42 = Miasto(nazwa_miasta = "Koszyce", kraj = słowacja)
        nM43 = Miasto(nazwa_miasta = "Preszów", kraj = słowacja)
        nM44 = Miasto(nazwa_miasta = "Żylina", kraj = słowacja)
        nM51 = Miasto(nazwa_miasta = "Wilno", kraj = litwa)
        nM52 = Miasto(nazwa_miasta = "Kowno", kraj = litwa)
        nM53 = Miasto(nazwa_miasta = "Kłajpeda", kraj = litwa)
        nM54 = Miasto(nazwa_miasta = "Szawle", kraj = litwa)
        nM61 = Miasto(nazwa_miasta = "Praga", kraj = czechy)
        nM62 = Miasto(nazwa_miasta = "Brno", kraj = czechy)
        nM63 = Miasto(nazwa_miasta = "Ostrawa", kraj = czechy)
        nM64 = Miasto(nazwa_miasta = "Pilzno", kraj = czechy)
        nM71 = Miasto(nazwa_miasta = "Mińsk", kraj = białoruś)
        nM72 = Miasto(nazwa_miasta = "Homel", kraj = białoruś)
        nM73 = Miasto(nazwa_miasta = "Grodno", kraj = białoruś)
        nM74 = Miasto(nazwa_miasta = "Witebsk", kraj = białoruś)
        db.session.add_all([noweMiasto1, nM2, nM3, nM4, nM5, nM6, nM7, nM8, nM11, nM12, nM13, nM14, nM21, nM22, nM23, nM24, nM31, nM32, nM33, nM34, nM41, nM42, nM43, nM44, nM51, nM52, nM53, nM54, nM61, nM62, nM63, nM64, nM7, nM72, nM73, nM74])



        nowyStanpogody1 = stanpogody(stan_pogody = 'pogodnie')
        nS2 = stanpogody(stan_pogody = 'deszcz')
        nS3 = stanpogody(stan_pogody = 'burza')
        nS4 = stanpogody(stan_pogody = 'śnieg')
        nS5 = stanpogody(stan_pogody = 'mgliście')
        nS6 = stanpogody(stan_pogody = 'pochmurnie')
        nS7 = stanpogody(stan_pogody = 'mżawka')
        db.session.add_all([nowyStanpogody1, nS2, nS3, nS4, nS5, nS6, nS7])



        nowyAtrybut1 = Atrybut(nazwa_atrybutu = "Temperatura")
        nA2 = Atrybut(nazwa_atrybutu = "Ciśnienie")
        nA3 = Atrybut(nazwa_atrybutu = "Prędkość wiatru")
        nA4 = Atrybut(nazwa_atrybutu = "Wilgotność")
        db.session.add_all([nowyAtrybut1, nA2, nA3, nA4])



        temperatura = db.session.query(Atrybut).filter_by(nazwa_atrybutu="Temperatura").first()
        ciśnienie = db.session.query(Atrybut).filter_by(nazwa_atrybutu="Ciśnienie").first()
        prędkość_wiatru = db.session.query(Atrybut).filter_by(nazwa_atrybutu="Prędkość wiatru").first()
        wilgotność = db.session.query(Atrybut).filter_by(nazwa_atrybutu="Wilgotność").first()

        nowaJednostka1 = Jednostka(nazwa_jednostki = "C", atrybut = temperatura)
        nJ2 = Jednostka(nazwa_jednostki = "F", atrybut = temperatura)
        nJ3 = Jednostka(nazwa_jednostki = "hPa", atrybut = ciśnienie)
        nJ4 = Jednostka(nazwa_jednostki = "km/h", atrybut = prędkość_wiatru)
        nJ5 = Jednostka(nazwa_jednostki = "mph", atrybut = prędkość_wiatru)
        nJ6 = Jednostka(nazwa_jednostki = "%", atrybut = wilgotność)
        db.session.add_all([nowaJednostka1, nJ2, nJ3, nJ4, nJ5, nJ6])



        nowyUser1 = User(email = "mikolaj56@vp.pl", username = "mikolaj", password = "haslo123")
        nU2 = User(email = "167833@stud.prz.edu.pl", username = "marek", password = "haslo123")
        nU3 = User(email = "167826@stud.prz.edu.pl", username = "agata", password = "kotek")
        db.session.add_all([nowyUser1, nU2, nU3])
          
        mikolaj = db.session.query(User).filter_by(username="mikolaj").first()
        rzeszow = db.session.query(Miasto).filter_by(nazwa_miasta="Rzeszów").first()
        warszawa = db.session.query(Miasto).filter_by(nazwa_miasta="Warszawa").first()
        gdansk = db.session.query(Miasto).filter_by(nazwa_miasta="Gdańsk").first()

        dtemp = db.session.query(Jednostka).filter_by(nazwa_jednostki="C").first()
        dcis = db.session.query(Jednostka).filter_by(nazwa_jednostki="hPa").first()
        dpred = db.session.query(Jednostka).filter_by(nazwa_jednostki="km/h").first()
        dwil = db.session.query(Jednostka).filter_by(nazwa_jednostki="%").first()

        #przypisywanie miast do uzytkownika/uzytkownikow do miasta
        for i in [rzeszow, warszawa]:
            mikolaj.miasta.append(i)
        gdansk.uzytkownicy.append(mikolaj)
        mikolaj.preferencje.extend([dtemp, dcis, dpred, dwil]) #append do pojedynczych, extend do list

        for i in dane['daily']:
            #print(i['weather'][0]['main'])
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
            #print(stan)
            nowaPogodaDzienna = PogodaDzienna(data = datetime.utcfromtimestamp(i['dt']),min_temp = i['temp']['min'],max_temp = i['temp']['max'], miasto = rzeszow, id_stan_pogody=stan)

        for i in dane['hourly']:
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
            nowaPogodaGodzinowa = PogodaGodzinowa(data = datetime.utcfromtimestamp(i['dt']), temperatura = i['temp'], predkosc_wiatru = i['wind_speed'], cisnienie = i['pressure'], miasto = rzeszow, id_stan_pogody = stan)

        db.session.commit()