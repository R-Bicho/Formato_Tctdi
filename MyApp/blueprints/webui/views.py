from flask import render_template, request
from flask import Blueprint

bp = Blueprint("webui", __name__)  



def init_app(app):    
    app.register_blueprint(bp)
    @bp.route("/")
    def index():
        titulo = 'Home'


        return render_template('index.html', titulo = titulo)
    
