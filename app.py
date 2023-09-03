
from flask import Flask, jsonify
from flask_restful import Api
from resources.users import UserRegister, UserLogin

from flask_swagger_ui import get_swaggerui_blueprint

from db import db

SWAGGER_URL = '/api/docs'  
API_URL = '/static/api_doc.json'  

swaggerui_blueprint = get_swaggerui_blueprint(
    # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    SWAGGER_URL,
    API_URL,
    config={  # Swagger UI config overrides
        'app_name': "Test application"
    },

)

app = Flask(__name__)
app.register_blueprint(swaggerui_blueprint)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['BUNDLE_ERRORS'] = True #global setting for all the reqparsers in the app
api = Api(app)

app.config['JWT_SECRET_KEY'] = 'lincoln'


api.add_resource(UserRegister, '/register')
api.add_resource(UserLogin, '/login')

if __name__ == '__main__':
    db.init_app(app)
    app.run(port = 8080, debug = True)


