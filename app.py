from flask import Flask, render_template, request, redirect, url_for, session
from models import db, Usuario, Cliente
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.secret_key = "sua_chave_secreta_123"

# Configuração do MySQL com URL encode para caracteres especiais
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/erp_db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Senai%40118@localhost/erp_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa extensões
bcrypt = Bcrypt(app)
db.init_app(app)

# Registra o blueprint do cliente
from clientes import clientes_bp # type: ignore
app.register_blueprint(clientes_bp)

# Registra o blueprint do usuário
from usuarios import usuarios_bp # type: ignore
app.register_blueprint(usuarios_bp)

# Registra o blueprint dos produtos
from produtos import produtos_bp # type: ignore
app.register_blueprint(produtos_bp)

# Registra o blueprint do pedido
from pedidos import pedidos_bp
app.register_blueprint(pedidos_bp)

@app.route('/')
def index():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('index.html')

# Rotas de login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = Usuario.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            session['logged_in'] = True
            session['username'] = username
            return redirect(url_for('index'))
        else:
            return render_template('login.html', erro="Usuário ou senha inválidos")
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

# Cria as tabelas e insere usuário admin
with app.app_context():
    db.create_all()
    if not Usuario.query.filter_by(username='admin').first():
        hashed_password = bcrypt.generate_password_hash('123456').decode('utf-8')
        admin = Usuario(username='admin', password=hashed_password)
        db.session.add(admin)
        db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)