from flask import Blueprint, redirect, render_template, request

from blueprints.classes.factory import tctdiFactory, volte
from blueprints.textos.textos_rotas import *

bp_tctdi = Blueprint("tctdi", __name__, template_folder='templates')

valores_formulario = []

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

    match tipo_telefone:
        case "pos":
            bo = '306'
            valores_formulario.append(bo)
        case "fixo":
            bo = '445'
            valores_formulario.append(bo)         
        case _:
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
                                              valores_formulario[5],
                                              valores_formulario[6])
    
    if  type(resultado) is volte:
        teste = formatoTctdiVolte(resultado)

        if len(teste) == 2:
            site1, formato1 = teste
            site1 = f'Site: {site1}'
            return render_template('index.html',
                           site1=site1,
                           formato1 = formato1,
                           texto=Explicacao_geral,
                           texto1=Explicacao_ddd,
                           texto2=Explicacao_rn_rop
                           )
        site1, site2, formato1, formato2 = teste
        site1 = f'Site: {site1}'
        site2 = f'Site: {site2}' 
        
        return render_template('index.html',
                           site1=site1,
                           formato1 = formato1,
                           site2= site2,
                           formato2 = formato2,
                           texto=Explicacao_geral,
                           texto1=Explicacao_ddd,
                           texto2=Explicacao_rn_rop
                           )

    return render_template('index.html',
                           Resultado=resultado,
                           texto=Explicacao_geral,
                           texto1=Explicacao_ddd,
                           texto2=Explicacao_rn_rop
                           )



def formatoTctdiVolte(resultado):
    objetoVolte = resultado.TctdiVolte()

    lista = []

    controle = ''
    for valor in objetoVolte:
        if valor != ',':
             controle += valor
        else:
             temporaria = controle.split()
             lista.append(temporaria)
             controle = ''
             continue           

    if len(lista) == 8:
        site1 = lista[0][0]
        site2 = lista[4][1]
        formato1 = f'{lista[0][1]}, {lista[1][0]}, {lista[2][0]}, {lista[3][0]} {lista[3][1]} {lista[3][2]} {lista[3][3]}, {lista[4][0]}'
        formato2 = f'{lista[4][2]}, {lista[5][0]}, {lista[6][0]}, {lista[7][0]} {lista[7][1]} {lista[7][2]} {lista[7][3]}, cl=1;'
        return site1, site2, formato1, formato2        
    
    site1 = f'{lista[0][0]}'
    formato1 = f'{lista[0][1]}, {lista[1][0]}, {lista[2][0]}, {lista[3][0]} {lista[3][1]} {lista[3][2]} {lista[3][3]}, cl=1; '
    return site1, formato1    