from flask import Blueprint, render_template, request, redirect, url_for
from .models import User, Kraj, Miasto, Atrybut, Jednostka, stanpogody, PogodaDzienna, PogodaGodzinowa
from . import db
from flask_login import login_user, current_user
from flask_mail import Mail, Message
from . import mail
from flask import current_app as app
from datetime import datetime

views = Blueprint("views", __name__)


@views.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        citi = request.form.get('miasto_data')
        citi2 = request.form.get('miasto_data2')
        print(citi)
        print(citi2)
    return render_template('./home/home.html', user=current_user, cities=db.session.query(Miasto).all(),dane=db.session.query(Miasto).filter_by(nazwa_miasta=citi).first())

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
