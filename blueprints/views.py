from flask import Blueprint, redirect, render_template, request

from blueprints.classes.tctdi import FormatoTctdi

bp_tctdi = Blueprint("tctdi", __name__, template_folder='templates')

valores_formulario = []


@bp_tctdi.route("/")
def index():
    titulo = 'Home'

    return render_template('index.html', titulo=titulo)


@bp_tctdi.route('/validar', methods=['POST', ])
def validar():

    valores_formulario.clear()
    try:
        tipo_telefone = request.form['valor']
    except KeyError:
        return render_template('index.html',
                               Resultado='Selecione um valor no campo \
                                Categoria Origem')

    numeroA = request.form['numeroA']

    if tipo_telefone == "fixo" and len(numeroA) > 10:
        return render_template('index.html',
                               Resultado='Digite um numero fixo válido')

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
    resultado = FormatoTctdi(valores_formulario[0],
                             valores_formulario[1],
                             valores_formulario[2],
                             valores_formulario[3],
                             valores_formulario[4],
                             valores_formulario[5])

    return render_template('index.html',
                           Resultado=resultado.retorno_formato(),
                           formulario=valores_formulario)
