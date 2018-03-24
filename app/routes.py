from app import app2 as app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm, RegistrationForm
from app.models import posts1, User, db, plans1, posts2, posts3, posts4, posts5, posts6, plans2, plans3, plans4, plans5, plans6
from flask_login import current_user, login_user, logout_user


@app.route('/')
@app.route('/index')
def Index():
    user2 = {'username4': 'Club CPQ'}

    a3title = {'username15': 'CPQ'}

    return render_template('index.html', user1=user2, title=a3title)

@app.route('/plans2')
def Plans2():
    user2 = {'username4': 'Club CPQ'}

    a3title = {'username15': 'CPQ'}

    posts31 = plans1.query.all()
    posts32 = plans2.query.all()
    posts33 = plans3.query.all()
    posts34 = plans4.query.all()
    posts35 = plans5.query.all()
    posts36 = plans6.query.all()

    return render_template('plans2.html', user1=user2, posts61=posts31, posts62=posts32, posts63=posts33, posts64=posts34, posts65=posts35, posts66=posts36, title=a3title)


@app.route('/plans')
def store():
    if current_user.is_authenticated:
        return redirect(url_for('Plans2'))

    else:
        user2 = {'username4': 'Club CPQ'}

        a3title = {'username15': 'CPQ'}

        posts21 = posts1.query.all()
        posts22 = posts2.query.all()
        posts23 = posts3.query.all()
        posts24 = posts4.query.all()
        posts25 = posts5.query.all()
        posts26 = posts6.query.all()

        return render_template('plans.html', user1=user2, posts51=posts21, posts52=posts22, posts53=posts23, posts54=posts24, posts55=posts25, posts56=posts26,title=a3title)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('Index'))
    form = LoginForm()
    if form.validate_on_submit():  # post and submit validate

        # get the user from data base use code
        user = User.query.filter_by(username=form.username.data).first()

        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))

        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('Index'))

    return render_template('login.html', title='Sign In', form=form)  # GET or submit validate Flaid


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('Index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('Index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)

        db.session.add(user)
        db.session.commit()  # this stuff puts the user in the database

        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/details')
def details():
    user2 = {'username4': 'Club CPQ'}

    a3title = {'username15': 'CPQ'}
    return render_template('details.html', user1=user2, title=a3title)

@app.route('/details2')
def details2():
    user2 = {'username4': 'Club CPQ'}

    a3title = {'username15': 'CPQ'}
    return render_template('details2.html', user1=user2, title=a3title)

@app.route('/details3')
def details3():
    user2 = {'username4': 'Club CPQ'}

    a3title = {'username15': 'CPQ'}
    return render_template('details3.html', user1=user2, title=a3title)

@app.route('/details4')
def details4():
    user2 = {'username4': 'Club CPQ'}

    a3title = {'username15': 'CPQ'}
    return render_template('details4.html', user1=user2, title=a3title)

@app.route('/details5')
def details5():
    user2 = {'username4': 'Club CPQ'}

    a3title = {'username15': 'CPQ'}
    return render_template('details5.html', user1=user2, title=a3title)

@app.route('/details6')
def details6():
    user2 = {'username4': 'Club CPQ'}

    a3title = {'username15': 'CPQ'}
    return render_template('details6.html', user1=user2, title=a3title)