from sqlalchemy.orm import backref
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))




class User(UserMixin,db.Model):
    __tablename__= 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))
    blog = db.relationship('Blog',backref = 'user_blog', lazy="dynamic") 
    comments = db.relationship('Comment',backref = 'user',lazy = "dynamic")

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
    blog = db.relationship('Blog',backref = 'blog', lazy="dynamic") 

    def __repr__(self):
        return f'{self.category_name}'


class BLog(db.Model):
    __tablename__='blog'

    id = db.Column(db.Integer,primary_key = True)
    blog_title = db.Column(db.String(255))
    blog_content = db.Column(db.String(255))
    category = db.Column(db.Integer, db.ForeignKey('category.id'))
    blog_author = db.Column(db.Integer, db.ForeignKey('users.id'))
    vote = db.relationship('Vote',backref = 'vote', lazy="dynamic") 
    comment = db.relationship('Comment',backref = 'comments', lazy="dynamic") 

    def __repr__(self):
        return f'Blog{self.pitch_title}'


class Vote(db.Model):
    __tablename__='vote'

    id = db.Column(db.Integer,primary_key = True)
    upvote = db.Column(db.String(255))
    downvote = db.Column(db.String(255))
    blog = db.Column(db.Integer, db.ForeignKey('blog.id'))
    author = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return f'Blog{self.upvote}'

class Comment(db.Model):

    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key = True)
    comment = db.Column(db.String)
    blog = db.Column(db.Integer, db.ForeignKey('blog.id'))
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,id):
        comments = Comment.query.filter_by(blog=id).all()
        return comments
