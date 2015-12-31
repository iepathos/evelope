import flask, flask.views, settings

class Login(flask.views.MethodView):
    def get(self):
        return flask.render_template('login.html', title='Log In',)

    def post(self):
        required = ['username', 'passwd']
        for r in required:
            if r not in flask.request.form:
                flask.flash("Error: {0} is required.".format(r))
                return flask.redirect(flask.url_for('main'))
        username = flask.request.form['username']
        passwd = flask.request.form['passwd']
        if username in settings.users and settings.users[username] == passwd:
            flask.session['username'] = username
        else:
            flask.flash("Username or password incorrect")
        return flask.redirect(flask.url_for('main'))
