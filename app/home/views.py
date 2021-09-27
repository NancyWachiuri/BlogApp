from flask import render_template, request, redirect, url_for
from . import home
from flask_login import login_required
from .forms import CategoryForm
from ..models import Category
from .. import db

@login_required
@home.route('/')
def index():
    return render_template("home/index.html")


@login_required
@home.route('/add_category')
def add_category():
    form = CategoryForm()
    if form.validate_on_submit():
        category = Category(category_name = form.category_name.data)
        db.session.add(category)
        db.session.commit()
        return redirect(url_for('home.index'))

    return render_template("home/add_category.html")

