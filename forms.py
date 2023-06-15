from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from flask_wtf.file import FileField, FileRequired, FileAllowed


class formLogin(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    senha = PasswordField('Senha', validators=[DataRequired(),Length(6, 12)])
    submitLogin = SubmitField('Login')
    

class formNovoUsuario(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(),Email()])
    celular = StringField('Celular', validators=[])
    cpf = StringField('CPF', validators=[])
    senha = PasswordField('Senha', validators=[DataRequired(),Length(6, 12)])
    senhaConfirmacao = PasswordField('Confirmaçao de Senha',validators=[DataRequired(),EqualTo('senha')])
    submit = SubmitField('Criar Conta')

class formCadastroProduto(FlaskForm):
    nome = StringField('nome', validators=[DataRequired()])
    descricao = StringField('descricao', validators=[DataRequired()])
    imagem = FileField('imagem', validators=[FileRequired('informa uma imagem')])
    submit = SubmitField('Cadastro Produto')