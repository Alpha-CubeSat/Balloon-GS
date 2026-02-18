from apifairy import APIFairy #A REST API documentation + validation helper.
from flask import Flask, redirect, url_for #creates web application object
from flask_cors import CORS
from flask_marshmallow import Marshmallow # Python to JSON serialization,define schemas
from werkzeug.middleware.proxy_fix import ProxyFix # Handle some client API corretions

from config import Config

ma = Marshmallow()
apifairy = APIFairy()
cors = CORS()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.wsgi_app = ProxyFix(app.wsgi_app, x_prefix=1)
    ma.init_app(app)
    apifairy.init_app(app)
    cors.init_app(app)

    from api.auth import auth
    app.register_blueprint(auth, url_prefix='/api/auth')
    #from api.user import user
    #app.register_blueprint(user, url_prefix='/api/user')
    #from api.cubesat import cubesat
    #app.register_blueprint(cubesat, url_prefix='/api/cubesat')
    from api.errors import errors
    app.register_blueprint(errors)

    from . import users_db
    users_db.init_app(app)

    @app.route('/')
    @app.route('/api')
    def index():
        return redirect(url_for('apifairy.docs'))

    @app.get('/ping')
    def ping():
        return {'response': 'pong'}

    return app