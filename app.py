from flask import Flask, render_template
from forms import formLogin, formNovoUsuario


app = Flask(__name__)

app.config['SECRET_KEY'] = '997181c5137d5ee684f482e6274956e4861e3460653aa4c5317d7065bef83c7c'

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
    return render_template('login.html',titulo=titulo,descricao=descricao,form_login=form_login,form_novo_usuario=form_novo_usuario)


if __name__=='__main__':
    app.run(debug=True)

