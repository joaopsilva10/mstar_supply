from flask import Blueprint, request, jsonify
from app.models import db, Mercadoria, Entrada, Saida
from datetime import datetime

main = Blueprint('main', __name__)

def validar_campos_mercadoria(data):
    """Valida se os campos obrigatórios da mercadoria estão preenchidos."""
    required_fields = ['nome', 'numero_registro', 'fabricante', 'tipo']
    for field in required_fields:
        if field not in data or data[field] == '':
            return f'O campo {field} é obrigatório.'
    return None

def validar_data(data_hora_str):
    """Valida se a data está no formato correto."""
    try:
        datetime.strptime(data_hora_str, '%Y-%m-%d %H:%M:%S')
    except ValueError:
        return 'O formato da data deve ser YYYY-MM-DD HH:MM:SS.'
    return None

@main.route('/mercadorias', methods=['POST'])
def cadastrar_mercadoria():
    data = request.get_json()

    # Validação de campos obrigatórios
    erro = validar_campos_mercadoria(data)
    if erro:
        return jsonify({'message': erro}), 400

    nova_mercadoria = Mercadoria(
        nome=data['nome'],
        numero_registro=data['numero_registro'],
        fabricante=data['fabricante'],
        tipo=data['tipo'],
        descricao=data.get('descricao')
    )

    try:
        db.session.add(nova_mercadoria)
        db.session.commit()
        return jsonify({'message': 'Mercadoria cadastrada com sucesso!'}), 201
    except Exception as e:
        db.session.rollback()  # Desfaça a transação em caso de erro
        return jsonify({'error': str(e)}), 500

@main.route('/entradas', methods=['POST'])
def cadastrar_entrada():
    data = request.get_json()

    # Validação de campos obrigatórios
    if 'quantidade' not in data or data['quantidade'] <= 0:
        return jsonify({'message': 'O campo quantidade é obrigatório e deve ser maior que zero.'}), 400
    
    if 'local' not in data or data['local'] == '':
        return jsonify({'message': 'O campo local é obrigatório.'}), 400
    
    if 'mercadoria_id' not in data or data['mercadoria_id'] <= 0:
        return jsonify({'message': 'O campo mercadoria_id é obrigatório e deve ser maior que zero.'}), 400

    # Validação do formato da data
    erro = validar_data(data['data_hora'])
    if erro:
        return jsonify({'message': erro}), 400

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

    # Validação de campos obrigatórios
    if 'quantidade' not in data or data['quantidade'] <= 0:
        return jsonify({'message': 'O campo quantidade é obrigatório e deve ser maior que zero.'}), 400
    
    if 'local' not in data or data['local'] == '':
        return jsonify({'message': 'O campo local é obrigatório.'}), 400
    
    if 'mercadoria_id' not in data or data['mercadoria_id'] <= 0:
        return jsonify({'message': 'O campo mercadoria_id é obrigatório e deve ser maior que zero.'}), 400

    # Validação do formato da data
    erro = validar_data(data['data_hora'])
    if erro:
        return jsonify({'message': erro}), 400

    saida = Saida(
        quantidade=data['quantidade'],
        data_hora=datetime.strptime(data['data_hora'], '%Y-%m-%d %H:%M:%S'),
        local=data['local'],
        mercadoria_id=data['mercadoria_id']
    )
    db.session.add(saida)
    db.session.commit()
    return jsonify({'message': 'Saída registrada com sucesso!'}), 201