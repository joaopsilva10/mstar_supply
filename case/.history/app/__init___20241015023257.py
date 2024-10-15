from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # Configuração do banco de dados
    app.config.from_object('app.config.Config')

    # Inicializa as extensões
    db.init_app(app)
    migrate.init_app(app, db)

    from app.routes import main
    app.register_blueprint(main)

    # Importa as rotas  
    with app.app_context():
        from app import routes  # Importa as rotas

    return app
