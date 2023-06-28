from flask import Flask, Blueprint, render_template, request, redirect
#from gerador_senha import retornoSenha
from blueprints.funcoes.setdb import setDB
import re

bp_login = Blueprint("login", __name__, template_folder='templates')


@bp_login.route('/')
@bp_login.route('/login')
def index():  
    return render_template('login.html')                           

@bp_login.route('/validar-login', methods=['POST',])
def validarLogin():
    matricula = request.form['matricula']
    senha = request.form['senha']
    
    return render_template('login.html',
                           matricula = matricula,
                           senha = senha)


@bp_login.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@bp_login.route('/validar-cadastro', methods=['POST',])
def validarCadastro():
    matricula = request.form['matricula']
    email = request.form['email']
    senha = request.form['senha']
    confirmar_senha = request.form['confirmar_senha']

    if senha == confirmar_senha:
        setDB(matricula, email, senha)
        return render_template('cadastro.html',
                               retorno = 'Sucesso')

    return render_template('cadastro.html',
                           retorno = 'Verifique os valores digitados')


@bp_login.route('/reset-senha')
def senha():
    return render_template('reset_senha.html')

@bp_login.route('/validar-email', methods=['POST',])
def validarSenha():
    email = request.form['email']    

    email_regexp = re.compile(r'^[A-Za-z]*@timbrasil\.com\.br$')

    if email_regexp.search(email):
        return redirect('/nova-senha')
    return render_template('reset_senha.html', email='Verificar e-mail')

@bp_login.route('/nova-senha')
def senha1():
    return render_template('nova_senha.html')


if __name__=='__main__':
    bp_login.run(debug=True)