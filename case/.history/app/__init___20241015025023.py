from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()  # Instância do SQLAlchemy
migrate = Migrate()  # Instância do Flask-Migrate

def create_app():
    app = Flask(__name__)

    # Configuração do banco de dados
    app.config.from_object('app.config.Config')

    # Inicializa as extensões
    db.init_app(app)  # Certifique-se de que isso está aqui
    migrate.init_app(app, db)  # Inicializa o Flask-Migrate com o app e db

    # Importa e registra as rotas
    from app.routes import main
    app.register_blueprint(main)

    return app