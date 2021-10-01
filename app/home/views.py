from flask import render_template, request, redirect, url_for
from . import home
from flask_login import login_required, current_user
from .forms import CategoryForm, BlogForm, CommentForm
from ..models import Category, Comment,Blog, Vote
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
@home.route('/add_blog', methods=['GET','POST'])
def add_blog():
    form = BlogForm()
    if form.validate_on_submit():
        new_blog = Blog(
            blog_title = form.blog_title.data, 
            blog_content = form.blog_content.data, 
            category= form.category_name.data.id,
            blog_author=current_user.id )
        db.session.add(new_blog)
        db.session.commit()
        return redirect(url_for('home.index'))
    return render_template("home/blog.html", blog_form=form)

@home.route('/upvote/<int:blog_id>')
@login_required
def upvote(blog_id):
    blog=Blog.query.filter_by(id=blog_id).first()
    print(blog.blog_title)
    myvote = 1
    vote = Vote(upvote=myvote, author = current_user.id, blog = blog_id)
    db.session.add(vote)
    db.session.commit()
    return redirect(url_for("home.index"))


@home.route('/downvote/<int:blog_id>')
@login_required
def downvote(blog_id):
    blog=Blog.query.filter_by(id=blog_id).first()
    print(blog.blog_title)
    mydownvote = 1
    vote = Vote(downvote=mydownvote, author = current_user.id, blog = blog_id)
    db.session.add(vote)
    db.session.commit()
    return redirect(url_for("home.index"))


@home.route('/blog/comment/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_comment(id):
    form = CommentForm()
    blog = Blog.query.filter_by(id=id).first()
    if form.validate_on_submit():

        comment = form.comment_content.data

        new_comment = Comment(blog=blog.id,comment=comment,user_id=current_user.id)

        new_comment.save_comment()
        return redirect(url_for('.index',))

    title = 'comment'
    return render_template('home/new_comment.html', comment_form=form)


