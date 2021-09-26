from flask import render_template, request, redirect, url_for
from . import home

@home.route('/')
def index():
    return render_template("home/index.html")