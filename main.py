import flask, flask.views, settings, operator

class Main(flask.views.MethodView):
    def get(self):
        balance = 0
        piles = 0
        if 'username' in flask.session:
            logged_in = True
            balance = 0
            piles = {
                'rent' : 100000,
                'utilities' : 50000,
                'groceries' : 22500,
                'entertainment' : 14291,
                'gas' : 10000,
                'emergency' : 750000
            }
            # Add up all piles to get total balance #
            for pile in piles:
                balance = balance + piles[pile]
            # Sort Piles From Largest - Smallest by value #
            piles = sorted(piles.items(), key=operator.itemgetter(1))

        else:
            logged_in = False

        templateData = {
            'title' : 'Home',
            'logged_in' : logged_in,
            'total' : balance,
            'piles' : piles,
        }
        return flask.render_template('index.html', **templateData)
