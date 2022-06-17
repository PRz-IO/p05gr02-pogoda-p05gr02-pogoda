from flask import Blueprint, render_template, request, redirect, url_for
from sqlalchemy import false, true
from .models import User, Kraj, Miasto, Atrybut, Jednostka, stanpogody, PogodaDzienna, PogodaGodzinowa
from . import db
from flask_login import login_user, current_user, logout_user
from flask_mail import Mail, Message
from . import mail
from flask import current_app as app
from datetime import datetime

views = Blueprint("views", __name__)


@views.route('/wycieczka', methods=['GET', 'POST'])
def wycieczka():
    zmienna = false
    citi = ""
    citi2 = ""
    data = []
    pm1 = []
    pm2 = []
    if current_user.is_authenticated:
        for miasto in current_user.miasta:
            pogoda = miasto.pogoda_dzienna
            if(pogoda):
                for dzien in pogoda:
                    if(dzien.data.date() == datetime.today().date()):
                        data.append(miasto.nazwa_miasta)
                        data.append(dzien.min_temp)
                        data.append(dzien.max_temp)
                        data.append(dzien.stanpogody.stan_pogody)
            # data.append(miasto.nazwa_miasta)
            # data.append(miasto.pogoda_dzienna)

    if request.method == 'POST':
        zmienna = true
        citi = request.form.get('miasto_data')
        citi2 = request.form.get('miasto_data2')
        m1 = db.session.query(Miasto).filter_by(nazwa_miasta=citi).first()
        m2 = db.session.query(Miasto).filter_by(nazwa_miasta=citi2).first()

        pog1 = m1.pogoda_dzienna
        pog2 = m2.pogoda_dzienna
        if(pog1):
            for dzien1 in pog1:
                if(dzien1.data.date() == datetime.today().date()):
                    pm1.append(m1.nazwa_miasta)
                    pm1.append(dzien1.min_temp)
                    pm1.append(dzien1.max_temp)
                    pm1.append(dzien1.stanpogody.stan_pogody)
        if(pog2):
            for dzien2 in pog2:
                if(dzien2.data.date() == datetime.today().date()):
                    pm2.append(m2.nazwa_miasta)
                    pm2.append(dzien2.min_temp)
                    pm2.append(dzien2.max_temp)
                    pm2.append(dzien2.stanpogody.stan_pogody)
        print(citi)
        print(citi2)
    return render_template('./wycieczka/wycieczka.html',tabela=zmienna, user=current_user, cities=db.session.query(Miasto).all(), dane=db.session.query(Miasto).filter_by(nazwa_miasta=citi).first(), miasto=data, pogoda1=pm1, pogoda2=pm2)


@views.route('/ustawienia', methods=['GET', 'POST'])
def ustawienia():
    if request.method == 'POST':
        citi = request.form.get('miasto_data')
        dodawane_miasto = db.session.query(
            Miasto).filter_by(nazwa_miasta=citi).first()
        current_user.miasta.append(dodawane_miasto)
        db.session.commit()
    return render_template('./ustawienia/ustawienia.html',
                           user=current_user, cities=db.session.query(Miasto).all())


@views.route('/', methods=['GET', 'POST'])
def home():
    citi = ""
    data = []
    data2 = []
    data_city = []
    pm1 = []
    pm2 = []
    if current_user.is_authenticated:
        for miasto in current_user.miasta:
            pogoda = miasto.pogoda_dzienna
            if(pogoda):
                for dzien in pogoda:
                    if(dzien.data.date() >= datetime.today().date()):
                        data.append([miasto.nazwa_miasta, dzien.min_temp, dzien.max_temp, dzien.stanpogody.stan_pogody])
            # data.append(miasto.nazwa_miasta)
            # data.append(miasto.pogoda_dzienna)

        for miasto in current_user.miasta:
            pogoda = miasto.pogoda_godzinowa
            if(pogoda):
                for godzina in pogoda:
                    if(godzina.data.date() >= datetime.today().date()):
                        data2.append(miasto.nazwa_miasta)
                        data2.append(godzina.data.strftime("%H:%M:%S"))
                        data2.append(godzina.temperatura)
                        data2.append(godzina.predkosc_wiatru)
                        data2.append(godzina.cisnienie)
                        data2.append(godzina.stanpogody.stan_pogody)
            # data.append(miasto.nazwa_miasta)
            # data.append(miasto.pogoda_dzienna)

    if request.method == 'POST':
        citi = request.form.get('miasto_data')
        m1 = db.session.query(Miasto).filter_by(nazwa_miasta=citi).first()

        pog1 = m1.pogoda_dzienna
        if(pog1):
            for dzien1 in pog1:
                if(dzien1.data.date() >= datetime.today().date()):
                    pm1.append(m1.nazwa_miasta)
                    pm1.append(dzien1.min_temp)
                    pm1.append(dzien1.max_temp)
                    pm1.append(dzien1.stanpogody.stan_pogody)
        print(citi)

        pogoda = m1.pogoda_godzinowa
        if(pogoda):
            for godzina in pogoda:
                if(godzina.data.date() >= datetime.today().date()):
                    data2.append(godzina.data.strftime("%H:%M:%S"))
                    data2.append(godzina.temperatura)
                    data2.append(godzina.predkosc_wiatru)
                    data2.append(godzina.cisnienie)
                    data2.append(godzina.stanpogody.stan_pogody)
    return render_template('./home/home.html', user=current_user,
                           cities=db.session.query(Miasto).all(), dane=db.session.query(Miasto).filter_by(nazwa_miasta=citi).first(),
                           miasto=data, pogoda1=pm1, pogoda2=pm2, data2=data2, data_city=data_city)


@views.route('/testMail')
def test():
    users = db.session.query(User).all()
    # print(users) #jesli .all() albo .first() nie jest dopisane do query to wypisuje sql, tylko daje pytajniki

    # test maila
    #wiadomosc = Message('Dzień dobry', recipients=['167828@stud.prz.edu.pl'])
    # mail.send(wiadomosc)

    return render_template('./testMail/testMail.html', uzytkownicy=users)


@views.route('/signup', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        passwords = [request.form.get(
            'password1'), request.form.get('password1')]
        new_user = User(email=email, username=firstName, password=passwords[0])
        db.session.add(new_user)
        db.session.commit()
    return render_template('./signup/signup.html')


@views.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()
        if user:
            if user.password == password:
                login_user(user, remember=True)
                return redirect(url_for('views.home'))

    return render_template('./login/login.html')


@views.route('/logout', methods=['GET', 'POST'])
def logout():
    if current_user.is_authenticated:
        logout_user()
    return redirect('/login')
