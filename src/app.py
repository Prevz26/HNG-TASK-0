from flask import Flask
from api.exception import exception_blueprint
from api.extensions import *
from api.routes import api_blueprint

def create_app():
    app = Flask(__name__)
    ma.init_app(app)
    CORS(app, resources={r"*": {"origins": "*"}}, supports_credentials=True)

    #configure blueprint
    app.register_blueprint(exception_blueprint)
    app.register_blueprint(api_blueprint)
    return app 

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)