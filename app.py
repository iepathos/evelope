#!/usr/bin/env python
# -*- coding: utf-8 -*-
import flask.views, settings, utils, sqlite3
from flask.ext.assets import Environment, Bundle

# Views
from main import Main
from logout import Logout
from login import Login

app = flask.Flask(__name__)


# Converts amount in pennies to dollars.cents with formatting
def formatDollars(value):
    return '${:,.2f}'.format(value/100)
app.jinja_env.filters['formatDollars'] = formatDollars

assets = Environment(app)

css = Bundle('css/normalize.css', 'css/skeleton.css', 'css/custom.css', filters='cssmin', output='gen/packed.css')
assets.register('css_all', css)

app.secret_key = settings.secretKey
users = settings.users
DATABASE = settings.DATABASE


def connect_db():
    return sqlite3.connect(DATABASE)


# Routes
app.add_url_rule('/',
                    view_func=Main.as_view('main'),
                    methods=["GET", "POST"])
app.add_url_rule('/login',
                    view_func=Login.as_view('login'),
                    methods=["GET", "POST"])
app.add_url_rule('/logout',
                    view_func=Logout.as_view('logout'))

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=2525, debug=True)
