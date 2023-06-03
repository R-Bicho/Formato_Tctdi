from flask import render_template, request
from flask import Blueprint

bp_tctdi = Blueprint("tctdi", __name__, template_folder='templates') 


@bp_tctdi.route("/")
def index():
    titulo = 'Home'
        
    return render_template('index.html', titulo = titulo)
    
