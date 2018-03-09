from app import app2 as app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm, RegistrationForm
from app.models import Post, User, db
from flask_login import current_user, login_user, logout_user


@app.route('/')
@app.route('/index')
def Index():
    user2 = {'username4': 'moto'}

    a3title = {'username15': 'Dov'}

    posts2 = Post.query.all()

    return render_template('index.html', user1=user2, posts5=posts2, title=a3title)


@app.route('/plans')
def store():
    items6 = [
        {
            'title': "Python book",
            'price': "200"
        },
        {
            'title': "Cook book",
            'price': 2
        },
        {
            'title': "iphone X",
            'price': 1000
        }
    ]
    return render_template('plans.html', items5=items6)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():  # post and submit validate

        # get the user from data base use code
        user = User.query.filter_by(username=form.username.data).first()

        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))

        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))

    return render_template('login.html', title='Sign In', form=form)  # GET or submit validate Flaid


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)

        db.session.add(user)
        db.session.commit()  # this stuff puts the user in the database

        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)