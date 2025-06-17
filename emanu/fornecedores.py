from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import db, Fornecedor

fornecedores_bp = Blueprint('fornecedores_bp', __name__)

@fornecedores_bp.route('/fornecedores')
def fornecedores():
    fornecedores_lista = Fornecedor.query.all()
    return render_template('fornecedores.html', fornecedores=fornecedores_lista)

@fornecedores_bp.route('/fornecedores/novo')
def novo():
    return render_template('fornecedores_form.html', fornecedor=None)

@fornecedores_bp.route('/fornecedores/salvar', methods=['POST'])
def salvar():
    fornecedor = Fornecedor(
        nome=request.form['nome'],
        razão_social=request.form['razao_social'],
        email=request.form['email'],
        telefone=request.form['telefone'],
        celular=request.form.get('celular'),
        cnpj=request.form.get('cnpj'),
        IE=request.form.get('IE'),

        logradouro=request.form.get('logradouro'),
        numero=request.form.get('numero'),
        complemento=request.form.get('complemento'),
        cep=request.form.get('cep'),
        cidade=request.form.get('cidade'),
        uf=request.form.get('uf')
    )
    db.session.add(fornecedor)
    db.session.commit()
    flash("Fornecedor cadastrado com sucesso!", "success")
    return redirect(url_for('fornecedores_bp.fornecedores'))

@fornecedores_bp.route('/fornecedores/editar/<int:id>')
def editar(id):
    fornecedor = Fornecedor.query.get_or_404(id)
    return render_template('fornecedor_form.html', fornecedor=fornecedor)

@fornecedores_bp.route('/fornecedores/atualizar', methods=['POST'])
def atualizar():
    id = request.form['id']
    fornecedor = Fornecedor.query.get_or_404(id)

    fornecedor.nome = request.form['nome']
    fornecedor.razão_social = request.form['razao_social']
    fornecedor.email = request.form['email']
    fornecedor.telefone = request.form['telefone']
    fornecedor.celular = request.form.get('celular')
    fornecedor.cnpj = request.form.get('cnpj')
    fornecedor.IE = request.form.get('IE')
    

    fornecedor.logradouro = request.form.get('logradouro')
    fornecedor.numero = request.form.get('numero')
    fornecedor.complemento = request.form.get('complemento')
    fornecedor.cep = request.form.get('cep')
    fornecedor.cidade = request.form.get('cidade')
    fornecedor.uf = request.form.get('uf')

    db.session.commit()
    flash("Fornecedor atualizado com sucesso!", "success")
    return redirect(url_for('fornecedores_bp.fornecedores'))

@fornecedores_bp.route('/fornecedores/excluir/<int:id>')
def excluir(id):
    fornecedor = Fornecedor.query.get_or_404(id)

    if fornecedor.pedidos:
        flash("Não é possível excluir este cliente porque ele possui pedidos vinculados.", "danger")
        return redirect(url_for('fornecedores_bp.fornecedores'))

    db.session.delete(fornecedor)
    db.session.commit()
    flash("Fornecedor excluído com sucesso!", "success")
    return redirect(url_for('fornecedores_bp.fornecedores'))
