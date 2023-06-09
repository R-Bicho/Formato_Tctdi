from flask import Blueprint, redirect, render_template, request

from blueprints.classes.factory import tctdiFactory

bp_tctdi = Blueprint("tctdi", __name__, template_folder='templates')

valores_formulario = []
titulo = 'Home'
Explicacao_geral = 'Para cliente pré-pago é necessário utilizar \
    o comando xxxxxxxx para encontrar o BO e selecionar, após isso\
    deve selecionar opção correspondente no campo BO, \
    se o numero for pós-pago ou fixo não precisa selecionar'
Explicacao_ddd = 'Necessário preencher o campo DDD registrado \
    se o numero de origem estiver em um DDD diferente do nativo \
    (Ex: Numero origem 11999999999 porém registrado DDD 12) \
    caso contrário, pode deixar em branco'
Explicacao_rn_rop = 'Os campos RN e ROP só precisam ser preenchidos em numeros fixos'


@bp_tctdi.route("/")
def index():

    return render_template('index.html',
                           titulo=titulo,
                           texto=Explicacao_geral,
                           texto1=Explicacao_ddd,
                           texto2=Explicacao_rn_rop)


@bp_tctdi.route('/validar', methods=['POST', ])
def validar():

    valores_formulario.clear()

    try:
        tipo_telefone = request.form['valor']
    except KeyError:
        return redirect('/')

    numeroA = request.form['numeroA']

    if tipo_telefone == "fixo" and len(numeroA) > 10:
        return redirect('/')

    numeroB = request.form['numeroB']
    ddd_registrado = request.form['ddd']
    bo = request.form['bo']
    rn = request.form['rn']
    rop = request.form['rop']

    valores_formulario.append(numeroA)
    valores_formulario.append(numeroB)
    valores_formulario.append(ddd_registrado)

    if tipo_telefone == "pos":
        bo = '306'
        valores_formulario.append(bo)
    elif tipo_telefone == "fixo":
        bo = '445'
        valores_formulario.append(bo)
    else:
        valores_formulario.append(bo)

    valores_formulario.append(rn)
    valores_formulario.append(rop)
    valores_formulario.append(tipo_telefone)

    return redirect('/resultado')


@bp_tctdi.route('/resultado')
def resultado():
    resultado = tctdiFactory.criaFormatoTctdi(valores_formulario[0],
                                              valores_formulario[1],
                                              valores_formulario[2],
                                              valores_formulario[3],
                                              valores_formulario[4],
                                              valores_formulario[5])

    return render_template('index.html',
                           Resultado=resultado,
                           texto=Explicacao_geral,
                           texto1=Explicacao_ddd,
                           texto2=Explicacao_rn_rop
                           )
