import os

from flask import Flask


def create_app(test_config=None):
	# create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
            SECRET_KEY='dev',) # if necessary  SQLALCHEMY_DATABASE_URI='mysql://root:pass@localhost/project'
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure that the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'
#may need to remove the hello
    # from . import database
    # database.init_db()

    from . import auth
    app.register_blueprint(auth.bp)

    from . import dashboard
    app.register_blueprint(dashboard.bp)
    # app.add_url_rule('/', endpoint='index') # this adds a rule. this ensures that url_for('index') url_for('dashboard.index') build the same url: /index. it is at the root because it is the main thing in our blogging website. that's why it does not have a url prefix. refer that website for a better understanding.

    from . import landing
    app.register_blueprint(landing.bp)
    app.add_url_rule('/', endpoint='index')

    return app
