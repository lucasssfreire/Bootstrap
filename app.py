from flask import Flask, render_template

app = Flask(__name__)

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

@app.route("/login")
def login():
    titulo = 'Login de Acesso'
    descricao = 'Formulario de login'
    return render_template('login.html',titulo=titulo,descricao=descricao)


if __name__=='__main__':
    app.run(debug=True)

