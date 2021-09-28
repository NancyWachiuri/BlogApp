from flask import render_template, request, redirect, url_for
from . import home
from flask_login import login_required, current_user
from .forms import CategoryForm, PitchForm, CommentForm
from ..models import Category, Comment,Pitch, Vote
from .. import db

@login_required
@home.route('/')
def index():
    category = Category.query.all()
    return render_template("home/index.html", categories =category)


@login_required
@home.route('/add_category', methods = ['GET','POST'])
def add_category():
    form = CategoryForm()
    if form.validate_on_submit():
        category =Category(category_name = form.category_name.data)
        db.session.add(category)
        db.session.commit()
        return redirect(url_for('home.index'))
    return render_template("home/add_category.html", category_form = form)

@login_required
@home.route('/add_pitch', methods=['GET','POST'])
def add_pitch():
    form = PitchForm()
    if form.validate_on_submit():
        new_pitch = Pitch(
            pitch_title = form.pitch_title.data, 
            pitch_content = form.pitch_content.data, 
            category= form.category_name.data.id,
            pitch_author=current_user.id )
        db.session.add(new_pitch)
        db.session.commit()
        return redirect(url_for('home.index'))
    return render_template("home/pitch.html", pitch_form=form)

@home.route('/upvote/<int:pitch_id>')
@login_required
def upvote(pitch_id):
    pitch=Pitch.query.filter_by(id=pitch_id).first()
    print(pitch.pitch_title)
    myvote = 1
    vote = Vote(upvote=myvote, author = current_user.id, pitch = pitch_id)
    db.session.add(vote)
    db.session.commit()
    return redirect(url_for("home.index"))


@home.route('/downvote/<int:pitch_id>')
@login_required
def downvote(pitch_id):
    pitch=Pitch.query.filter_by(id=pitch_id).first()
    print(pitch.pitch_title)
    mydownvote = 1
    vote = Vote(downvote=mydownvote, author = current_user.id, pitch = pitch_id)
    db.session.add(vote)
    db.session.commit()
    return redirect(url_for("home.index"))


@home.route('/pitch/comment/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_comment(id):
    form = CommentForm()
    pitch = Pitch.query.filter_by(id=id).first()
    if form.validate_on_submit():

        comment = form.comment_content.data

        new_comment = Comment(pitch=pitch.id,comment=comment,user_id=current_user.id)

        new_comment.save_comment()
        return redirect(url_for('.index',))

    title = 'comment'
    return render_template('home/new_comment.html', comment_form=form)


