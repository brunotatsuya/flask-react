from flask import Flask
from flask_cors import CORS # comment this on deployment

from api.routes import init as init_routes
from api.page_routes import init as init_page_routes

def create_app():
    app = Flask(__name__, static_url_path='', static_folder='client/dist')
    CORS(app) # comment this on deployment
    init_routes(app)
    init_page_routes(app)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run()