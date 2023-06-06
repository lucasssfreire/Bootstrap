import mysql.connector
from flask import Flask, render_template, request, url_for, flash, redirect
from forms import formLogin, formNovoUsuario
from hashlib import sha256


app = Flask(__name__)

app.config['SECRET_KEY'] = '997181c5137d5ee684f482e6274956e4861e3460653aa4c5317d7065bef83c7c'

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'P@$$w0rd',
    database = 'ead_senac',
)

@app.route("/")
def index():
    return render_template('index.html')
 
@app.route("/sobreEAD")
def ead():
    return render_template('sobre_EAD.html') 

@app.route("/cursos")
def cursos():
    return render_template('cursos.html')

@app.route("/contato")
def contato():  
    return render_template('contato.html')

@app.route("/login", methods=['get','post'])
def login():
    titulo = 'Login de Acesso'
    descricao = 'Formulario de Login'

    form_login = formLogin()
    form_novo_usuario = formNovoUsuario()

    if form_login.validate_on_submit() and 'submitLogin' in request.form:

        flash(f'Login realizado com sucesso: {form_login.email.data}', 'alert-primary')
        return redirect(url_for('index'))

    if form_novo_usuario.validate_on_submit() and 'submit' in request.form:

        cursor = mydb.cursor()

        nome = form_novo_usuario.nome.data
        telefone = form_novo_usuario.celular.data
        email = form_novo_usuario.email.data
        cpf = form_novo_usuario.cpf.data
        senha = form_novo_usuario.senha.data
        hashSenha = sha256(senha.encode())
        query = f'INSERT INTO alunos (nome,email,celular,documento,senha) VALUES ("{nome}","{email}","{telefone}","{cpf}","{hashSenha.hexdigest()}")'
        cursor.execute(query)
        mydb.commit()

        flash(f'Cadastro realizadocom sucesso: {form_novo_usuario.nome.data}' , 'alert-success')
        return redirect(url_for('index'))

    return render_template('login.html',titulo=titulo,descricao=descricao,form_login=form_login,form_novo_usuario=form_novo_usuario)

if __name__=='__main__':
    app.run(debug=True)

