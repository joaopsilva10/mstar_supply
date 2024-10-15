from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Inicialize a instância do SQLAlchemy e Migrate fora da função create_app
db = SQLAlchemy() 
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # Carregue a configuração
    app.config.from_object('app.config.Config')

    # Inicialize as extensões
    db.init_app(app) 
    migrate.init_app(app, db)

    # Registre o blueprint
    from app.routes import main
    app.register_blueprint(main)

    return app
