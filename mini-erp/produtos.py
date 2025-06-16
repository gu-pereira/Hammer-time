from flask import Blueprint, render_template, request, redirect, url_for
from models import db, Produto

produtos_bp = Blueprint('produtos_bp', __name__)

@produtos_bp.route('/produtos')
def produtos():
    produtos_lista = Produto.query.all()
    return render_template('produtos.html', produtos=produtos_lista)

@produtos_bp.route('/produtos/novo')
def novo_produto():
    return render_template('produto_form.html', produto=None)

@produtos_bp.route('/produtos/salvar', methods=['POST'])
def salvar_produto():
    nome = request.form['nome']
    descricao = request.form['descricao']
    preco = float(request.form['preco'])
    estoque = int(request.form['estoque'])

    produto = Produto(nome=nome, descricao=descricao, preco=preco, estoque=estoque)
    db.session.add(produto)
    db.session.commit()
    return redirect(url_for('produtos_bp.produtos'))

@produtos_bp.route('/produtos/editar/<int:id>')
def editar_produto(id):
    produto = Produto.query.get_or_404(id)
    return render_template('produto_form.html', produto=produto)

@produtos_bp.route('/produtos/atualizar', methods=['POST'])
def atualizar_produto():
    id = request.form['id']
    produto = Produto.query.get_or_404(id)
    produto.nome = request.form['nome']
    produto.descricao = request.form['descricao']
    produto.preco = float(request.form['preco'])
    produto.estoque = int(request.form['estoque'])

    db.session.commit()
    return redirect(url_for('produtos_bp.produtos'))

@produtos_bp.route('/produtos/excluir/<int:id>')
def excluir_produto(id):
    produto = Produto.query.get_or_404(id)
    db.session.delete(produto)
    db.session.commit()
    return redirect(url_for('produtos_bp.produtos'))