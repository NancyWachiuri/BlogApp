from sqlalchemy.orm import backref
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))




class User(UserMixin,db.Model):
    __tablename__= 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))
    pitch = db.relationship('Pitch',backref = 'user_pitch', lazy="dynamic") 

    def __repr__(self):
        return f'User{self.username}'


    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)



class Category(db.Model):
    __tablename__='category'

    id = db.Column(db.Integer,primary_key = True)
    category_name = db.Column(db.String(255))
    pitch = db.relationship('Pitch',backref = 'pitch', lazy="dynamic") 

    def __repr__(self):
        return f'{self.category_name}'


class Pitch(db.Model):
    __tablename__='pitch'

    id = db.Column(db.Integer,primary_key = True)
    pitch_title = db.Column(db.String(255))
    pitch_content = db.Column(db.String(255))
    category = db.Column(db.Integer, db.ForeignKey('category.id'))
    pitch_author = db.Column(db.Integer, db.ForeignKey('users.id'))
    vote = db.relationship('Vote',backref = 'vote', lazy="dynamic") 

    def __repr__(self):
        return f'Pitch{self.pitch_title}'


class Vote(db.Model):
    __tablename__='vote'

    id = db.Column(db.Integer,primary_key = True)
    upvote = db.Column(db.String(255))
    downvote = db.Column(db.String(255))
    pitch = db.Column(db.Integer, db.ForeignKey('pitch.id'))
    author = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return f'Pitch{self.upvote}'
