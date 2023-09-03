from flask import Flask
from flask_restx import Api, Namespace, Resource
from flask_cors import CORS
from structlog import get_logger
from werkzeug.middleware.proxy_fix import ProxyFix

logger = get_logger(__name__)

# INITIALIZE APP
app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_port=1)

# LOAD THE CONFIG FROM CONFIG CLASS
app.config.from_object('server.config.DevelopmentConfig')

# CORS
cors = CORS()
cors.init_app(app, resources={"*" : {"origins" : "*"}})

# API
api = Api(version="1.0", title="Flask Restx", doc="/api/v1/docs")
api.init_app(app)
api_namespace = Namespace("api")

# RESOURCE 
class Ping(Resource):
    def get(self):
        logger.debug("Ping.GET")
        return { "message" : "pong"}, 200

# API ENDPOINTS
api_namespace.add_resource(Ping, "/ping")
api.add_namespace(api_namespace, path="/api/v1")
