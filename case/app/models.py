from . import db

class Mercadoria(db.Model):
    __tablename__ = 'mercadorias'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    numero_registro = db.Column(db.String(50), nullable=False)
    fabricante = db.Column(db.String(100), nullable=False)
    tipo = db.Column(db.String(50), nullable=False)
    descricao = db.Column(db.Text, nullable=True)

    entradas = db.relationship('Entrada', backref='mercadoria', lazy=True)
    saidas = db.relationship('Saida', backref='mercadoria', lazy=True)
    
    def __repr__(self):
        return f'<Mercadoria {self.nome}>'

class Entrada(db.Model):
    __tablename__ = 'entradas'

    id = db.Column(db.Integer, primary_key=True)
    quantidade = db.Column(db.Integer, nullable=False)
    data_hora = db.Column(db.DateTime, nullable=False)
    local = db.Column(db.String(100), nullable=False)
    mercadoria_id = db.Column(db.Integer, db.ForeignKey('mercadorias.id'), nullable=False)

    def __repr__(self):
        return f'<Entradas {self.nome}>'

class Saida(db.Model):
    __tablename__ = 'saidas'

    id = db.Column(db.Integer, primary_key=True)
    quantidade = db.Column(db.Integer, nullable=False)
    data_hora = db.Column(db.DateTime, nullable=False)
    local = db.Column(db.String(100), nullable=False)
    mercadoria_id = db.Column(db.Integer, db.ForeignKey('mercadorias.id'), nullable=False)

    def __repr__(self):
        return f'<Saidas {self.nome}>'
