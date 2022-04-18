from flask import Flask

def create_app():
    app = Flask(__name__)

    from .routes import routes
    from .home import home
    app.register_blueprint(home, url_prefix='/')
    app.register_blueprint(routes, url_prefix='/')

    return app