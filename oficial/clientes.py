from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import db, Cliente

clientes_bp = Blueprint('clientes_bp', __name__)

@clientes_bp.route('/clientes')
def clientes():
    clientes_lista = Cliente.query.all()
    return render_template('clientes.html', clientes=clientes_lista)

@clientes_bp.route('/clientes/novo')
def novo():
    return render_template('cliente_form.html', cliente=None)

@clientes_bp.route('/clientes/salvar', methods=['POST'])
def salvar():
    nome = request.form['nome']
    email = request.form['email']
    telefone = request.form['telefone']

    cliente = Cliente(nome=nome, email=email, telefone=telefone)
    db.session.add(cliente)
    db.session.commit()
    return redirect(url_for('clientes_bp.clientes'))

@clientes_bp.route('/clientes/editar/<int:id>')
def editar(id):
    cliente = Cliente.query.get_or_404(id)
    return render_template('cliente_form.html', cliente=cliente)

@clientes_bp.route('/clientes/atualizar', methods=['POST'])
def atualizar():
    id = request.form['id']
    cliente = Cliente.query.get_or_404(id)
    cliente.nome = request.form['nome']
    cliente.email = request.form['email']
    cliente.telefone = request.form['telefone']
    db.session.commit()
    return redirect(url_for('clientes_bp.clientes'))

# @clientes_bp.route('/clientes/excluir/<int:id>')
# def excluir(id):
#     cliente = Cliente.query.get_or_404(id)
#     db.session.delete(cliente)
#     db.session.commit()
#     return redirect(url_for('clientes_bp.clientes'))

@clientes_bp.route('/clientes/excluir/<int:id>')
def excluir(id):
    cliente = Cliente.query.get_or_404(id)

    # Verifica se o cliente tem pedidos associados
    if cliente.pedidos:
        flash("Não é possível excluir este cliente porque ele possui pedidos vinculados.", "danger")
        return redirect(url_for('clientes_bp.clientes'))
    
    db.session.delete(cliente)
    db.session.commit()
    flash("Cliente excluído com sucesso!", "success")
    return redirect(url_for('clientes_bp.clientes'))