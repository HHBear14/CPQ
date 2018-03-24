from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        if password == '666666': return True  # remove after testing is done on website
        return check_password_hash(self.password_hash, password)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class posts1(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    title = db.Column(db.String(20))
    subtitle = db.Column(db.String(40))
    body = db.Column(db.String(280))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post123 {}>'.format(self.body)

class posts2(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    title = db.Column(db.String(20))
    subtitle = db.Column(db.String(40))
    body = db.Column(db.String(280))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post123 {}>'.format(self.body)

class posts3(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    title = db.Column(db.String(20))
    subtitle = db.Column(db.String(40))
    body = db.Column(db.String(280))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post123 {}>'.format(self.body)

class posts4(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    title = db.Column(db.String(20))
    subtitle = db.Column(db.String(40))
    body = db.Column(db.String(280))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post123 {}>'.format(self.body)

class posts5(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    title = db.Column(db.String(20))
    subtitle = db.Column(db.String(40))
    body = db.Column(db.String(280))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post123 {}>'.format(self.body)

class posts6(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    title = db.Column(db.String(20))
    subtitle = db.Column(db.String(40))
    body = db.Column(db.String(280))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post123 {}>'.format(self.body)

class plans1(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20))
    subtitle = db.Column(db.String(40))
    body = db.Column(db.String(280))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
       return '<plans20 {}>'.format(self.body)

class plans2(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20))
    subtitle = db.Column(db.String(40))
    body = db.Column(db.String(280))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
       return '<plans20 {}>'.format(self.body)

class plans3(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20))
    subtitle = db.Column(db.String(40))
    body = db.Column(db.String(280))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
       return '<plans20 {}>'.format(self.body)

class plans4(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20))
    subtitle = db.Column(db.String(40))
    body = db.Column(db.String(280))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
       return '<plans20 {}>'.format(self.body)

class plans5(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20))
    subtitle = db.Column(db.String(40))
    body = db.Column(db.String(280))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
       return '<plans20 {}>'.format(self.body)

class plans6(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20))
    subtitle = db.Column(db.String(40))
    body = db.Column(db.String(280))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
       return '<plans20 {}>'.format(self.body)




