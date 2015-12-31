#!/usr/bin/env python
# -*- coding: utf-8 -*-
import flask.views, settings
from flask.ext.assets import Environment, Bundle
from flask import Flask
from utils import formatDollars
from core import db
from users import User

# Views
from main import Main
from logout import Logout
from login import Login




def route_app(app):
    app.add_url_rule('/',
                     view_func=Main.as_view('main'),
                     methods=["GET", "POST"])
    app.add_url_rule('/login',
                     view_func=Login.as_view('login'),
                     methods=["GET", "POST"])
    app.add_url_rule('/logout',
                     view_func=Logout.as_view('logout'))
    return app


def register_assets(app):
    app.jinja_env.filters['formatDollars'] = formatDollars

    assets = Environment(app)

    css = Bundle('css/normalize.css',
                 'css/skeleton.css',
                 'css/custom.css', filters='cssmin', output='gen/packed.css')
    assets.register('css_all', css)
    return app


def create_app():
    app = Flask(__name__)
    app.config.from_object('settings')
    route_app(app)
    register_assets(app)
    db.init_app(app)
    return app
