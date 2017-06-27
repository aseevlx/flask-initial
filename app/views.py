# -*- coding: utf-8 -*-
from flask import render_template, flash, redirect, url_for
from app import app, db
from models import *
from forms import *


@app.route('/', methods=['GET', 'POST'])
def index():
	title = 'Index'
    return render_template("index.html",
                           title=title)