from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from Config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

@app.route('/')
def index():
    return "Conexão com o banco de dados estabelecida!"

if __name__ == '__main__':
    app.run(debug=True)
