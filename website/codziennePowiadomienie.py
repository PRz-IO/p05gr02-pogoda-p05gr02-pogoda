from .models import User, Kraj, Miasto, Atrybut, Jednostka, stanpogody, PogodaDzienna, PogodaGodzinowa
from . import db
from flask_mail import Mail, Message 
from . import mail
#from flask import current_app as app
from datetime import datetime
#from threading import Thread
                # bez threadingu 5 maili wysyła się w ~13 sekund, z threadingiem ~7
# def wyslijMail_thread(wiadomosc,app):
#     with app.app_context():
#         mail.send(wiadomosc)
#         print(datetime.today().time())

def porada(pogoda): #do dokończenia
    if(pogoda.id_stan_pogody == 2 or pogoda.id_stan_pogody == 7):
        print("Zapowiada się na deszcz - weź parasol!")

    if(pogoda.id_stan_pogody == 5):
        print("Zapowiada się na mgłę - uważaj na drodze!")

    if(pogoda.poludnie > 25):
        print("Zapowiada się na gorący dzień")

    if(pogoda.poludnie < 10):
        print("Zapowiada się na chłodny dzień")


def powiadomieniePogodowe(app, db):
    with app.app_context():
        #pobieram używane miasta (miasta z przypisanymi użytkownikami)
        przypisane_miasta = db.session.query(Miasto).filter(Miasto.uzytkownicy!=None).all()
        for miasto in przypisane_miasta:
            print(miasto.nazwa_miasta)

        #pobieram pogodę dla każdego z miast
            pogoda = miasto.pogoda_dzienna
        #jeśli w bazie istnieją dane pogodowe, pobieram dane użytkowników
            if(pogoda):
                for dzien in pogoda:
        #pobieram dane tylko z dnia wysyłania powiadomienia
                    if(dzien.data.date() == datetime.today().date()):
                        print(dzien.data.date())

                        status = dzien.stanpogody.stan_pogody
                        minT = dzien.min_temp
                        maxT = dzien.max_temp
                        print(status + ' ' + str(minT) + ' ' + str(maxT))
                        porada(dzien)


                        # with mail.connect() as conn:
                        #     for uzytkownik in miasto.uzytkownicy:
                        #         #print(uzytkownik.username + ' ' + uzytkownik.email)
                        #         #print(miasto.uzytkownicy[0].email)
                        #         #if(uzytkownik.username == 'mikolaj'):
                        #         wiadomosc = Message("Powiadomienie o pogodzie - "+miasto.nazwa_miasta, recipients = ['167828@stud.prz.edu.pl'])
                        #         wiadomosc.html = "<h3>Dzień dobry "+ uzytkownik.username.capitalize() +",</h3><h4>Pogoda w miejscowości '"+ miasto.nazwa_miasta+"' zapowiada się na '"+ status +"'.</h4><h4> Minimalna temperatura dzisiaj to: "+str(int(minT))+"C, a maksymalna to: "+str(int(maxT))+"C.</h4></br><h4>Miłego dnia :)</h4>"
                        #         with app.open_resource('cat.jpg') as cat:
                        #             wiadomosc.attach('cat.jpg', 'image/jpeg', cat.read())
                        #         conn.send(wiadomosc)
                        #         print(datetime.today().time())


                        # for uzytkownik in miasto.uzytkownicy:
                        #     #print(uzytkownik.username + ' ' + uzytkownik.email)
                        #     #print(miasto.uzytkownicy[0].email)
                        #     #if(uzytkownik.username == 'mikolaj'):
                        #     wiadomosc = Message("Powiadomienie o pogodzie - "+miasto.nazwa_miasta, recipients = ['167828@stud.prz.edu.pl'])
                        #     wiadomosc.html = "<h3>Dzień dobry "+ uzytkownik.username.capitalize() +",</h3><h4>Pogoda w miejscowości '"+ miasto.nazwa_miasta+"' zapowiada się na '"+ status +"'.</h4><h4> Minimalna temperatura dzisiaj to: "+str(int(minT))+"C, a maksymalna to: "+str(int(maxT))+"C.</h4></br><h4>Miłego dnia :)</h4>"
                        #     with app.open_resource('cat.jpg') as cat:
                        #         wiadomosc.attach('cat.jpg', 'image/jpeg', cat.read())
                        #     thr = Thread(target = wyslijMail_thread, args = [wiadomosc,app])
                        #     thr.start()
                            
                                            
            
        
        #print(przypisane_miasta)