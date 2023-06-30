from flask import Flask, Blueprint, render_template, request, redirect
from blueprints.classes.gerador_senha import retornoSenha
from blueprints.funcoes.setDB import setDB, updateSenhaDB, updateSenhaTemporaria
from blueprints.funcoes.valoresDB import MatriculaDB, senhaDB,senhaTemporariaDB
from blueprints.funcoes.valoresDB import emailPorMatricula
from blueprints.funcoes.send_email import enviandoEmail, validandoEmail


bp_login = Blueprint("login", __name__, template_folder='templates')

valor_matricula = []
usuario_logado = []

@bp_login.route('/')
@bp_login.route('/login')
def index():  
    return render_template('login.html')                           

@bp_login.route('/validar-login', methods=['POST',])
def validarLogin():
    matricula = request.form['matricula']
    matricula.upper()
    senha = request.form['senha']

    if MatriculaDB(matricula) is True and senhaDB(senha) is True:
        usuario_logado.append(True)
        return redirect('/tctdi')
        
    if MatriculaDB(matricula) is True and senhaDB(senha) is False:
        valor_matricula.append(matricula) 
        return redirect('/primeiro-acesso')
       
    return render_template('login.html',
                           mensagem = 'Verifique os valores digitados')

@bp_login.route('/primeiro-acesso')
def primeiroAcesso():
    return render_template('primeiro_acesso.html')

@bp_login.route('/validar-senha', methods=['POST',])
def validarPrimeiroAcesso():
    senha_temporaria = request.form['senha_temporaria']
    senha = request.form['nova_senha']
    nova_senha = request.form['confirmar_senha']
    matricula = ''.join(valor_matricula)

    email = emailPorMatricula(matricula)    

    if senhaTemporariaDB(matricula) == senha_temporaria and senha == nova_senha:
        updateSenhaDB(senha, email)
        return redirect('/login')
    
    if len(senha) > 8:
        return render_template('primeiro_acesso.html', 
                               mensagem = 'Senha deve ter no maximo 8 caracteres')

    if senhaTemporariaDB(matricula) == senha_temporaria and senha != nova_senha:
        return render_template('primeiro_acesso.html', 
                               mensagem = 'Senha deve ser igual a confirmação')
    
    if senhaTemporariaDB(matricula) != senha_temporaria:
        return render_template('primeiro_acesso.html', 
                               mensagem = 'Senha temporaria deve ser igual a do e-mail')


@bp_login.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@bp_login.route('/validar-cadastro', methods=['POST',])
def validarCadastro():
    matricula = request.form['matricula']
    email = request.form['email']
    senha_temporaria = retornoSenha()
    senha_temporaria = str(senha_temporaria)

    if validandoEmail(email) is False:
        return redirect('/cadastro')

    setDB(matricula, email, senha_temporaria)
    enviandoEmail(email, senha_temporaria)    
    return redirect('/login')


@bp_login.route('/reset-senha')
def resetSenha():
    return render_template('reset_senha.html')

@bp_login.route('/validar-email', methods=['POST',])
def validarEmail():
    email = request.form['email']   

    if validandoEmail(email):
        senha_temporaria = retornoSenha()
        senha_temporaria = str(senha_temporaria)
        enviandoEmail(email, senha_temporaria)
        updateSenhaTemporaria(senha_temporaria, email)
        return redirect('/nova-senha')
    return render_template('reset_senha.html', email='Verificar e-mail')

@bp_login.route('/nova-senha')
def novaSenha():
    return render_template('primeiro_acesso.html')