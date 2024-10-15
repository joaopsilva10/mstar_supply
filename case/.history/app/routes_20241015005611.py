from flask import Blueprint, request, jsonify
from app.models import db, Mercadoria, Entrada, Saida
from datetime import datetime

main = Blueprint('main', __name__)

@main.route('/mercadorias', methods=['POST'])
def cadastrar_mercadoria():
    data = request.get_json()
    nova_mercadoria = Mercadoria(
        nome=data['nome'],
        numero_registro=data['numero_registro'],
        fabricante=data['fabricante'],
        tipo=data['tipo'],
        descricao=data.get('descricao')
    )
    db.session.add(nova_mercadoria)
    db.session.commit()
    return jsonify({'message': 'Mercadoria cadastrada com sucesso!'}), 201

@main.route('/entradas', methods=['POST'])
def cadastrar_entrada():
    data = request.get_json()
    entrada = Entrada(
        quantidade=data['quantidade'],
        data_hora=datetime.strptime(data['data_hora'], '%Y-%m-%d %H:%M:%S'),
        local=data['local'],
        mercadoria_id=data['mercadoria_id']
    )
    db.session.add(entrada)
    db.session.commit()
    return jsonify({'message': 'Entrada registrada com sucesso!'}), 201

@main.route('/saidas', methods=['POST'])
def cadastrar_saida():
    data = request.get_json()
    saida = Saida(
        quantidade=data['quantidade'],
        data_hora=datetime.strptime(data['data_hora'], '%Y-%m-%d %H:%M:%S'),
        local=data['local'],
        mercadoria_id=data['mercadoria_id']
    )
    db.session.add(saida)
    db.session.commit()
    return jsonify({'message': 'Saída registrada com sucesso!'}), 201
