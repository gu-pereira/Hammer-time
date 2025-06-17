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
    cliente = Cliente(
        nome=request.form['nome'],
        email=request.form['email'],
        telefone=request.form['telefone'],
        celular=request.form.get('celular'),
        cpf=request.form.get('cpf'),
        data_nascimento=request.form.get('data_nascimento'),

        logradouro=request.form.get('logradouro'),
        numero=request.form.get('numero'),
        complemento=request.form.get('complemento'),
        cep=request.form.get('cep'),
        cidade=request.form.get('cidade'),
        uf=request.form.get('uf')
    )
    db.session.add(cliente)
    db.session.commit()
    flash("Cliente cadastrado com sucesso!", "success")
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
    cliente.celular = request.form.get('celular')
    cliente.cpf_cnpj = request.form.get('cpf_cnpj')
    cliente.data_nascimento = request.form.get('data_nascimento')

    cliente.logradouro = request.form.get('logradouro')
    cliente.numero = request.form.get('numero')
    cliente.complemento = request.form.get('complemento')
    cliente.cep = request.form.get('cep')
    cliente.cidade = request.form.get('cidade')
    cliente.uf = request.form.get('uf')

    db.session.commit()
    flash("Cliente atualizado com sucesso!", "success")
    return redirect(url_for('clientes_bp.clientes'))

@clientes_bp.route('/clientes/excluir/<int:id>')
def excluir(id):
    cliente = Cliente.query.get_or_404(id)

    if cliente.pedidos:
        flash("Não é possível excluir este cliente porque ele possui pedidos vinculados.", "danger")
        return redirect(url_for('clientes_bp.clientes'))

    db.session.delete(cliente)
    db.session.commit()
    flash("Cliente excluído com sucesso!", "success")
    return redirect(url_for('clientes_bp.clientes'))
