from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

migrate = Migrate() 

def create_app():
    app = Flask(__name__)
    
    app.config.from_object('app.config.Config')
    
    db = SQLAlchemy(app)
    
    from app.routes import main
    app.register_blueprint(main)

    return app