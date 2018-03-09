from flask import Flask
from flask import render_template, flash, redirect
from Forms import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Dov Only'


@app.route('/')
@app.route('/Index')
def Index():
    user2 = {'username4': 'moto'}

    a3title = {'username15': 'Dov'}

    posts2 = [
        {
            'title': {'main': 'I hate Python', 'sub': 'this is a sad story'},
            'body': 'Python can do every thing. However, it is very hard.'
        },
        {
            'title': {'main': 'I love Python', 'sub': 'this is a happy story'},
            'body': 'Python can do every thing. However, it is very easy.'
        },
        {
            'title': {'main': 'I love C+', 'sub': 'this is a happy story'},
            'body': 'C+ can do every thing. However, it is very easy.'
        }
    ]

    return render_template('Index.html', user1=user2, posts5=posts2, title=a3title)


@app.route('/store')
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
    return render_template('store.html', items5=items6)


@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user{}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect('/login')
    return render_template('login.html', title='Sign In', form=form)


app.run()