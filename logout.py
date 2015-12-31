import flask, settings

class Logout(flask.views.MethodView):
    def get(self):
        flask.session.pop('username', None)
        return flask.redirect(flask.url_for('main'))
