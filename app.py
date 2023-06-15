from flask import Flask
from blueprints.views import bp_tctdi
from banco_dados import conexaoBanco

app = Flask(__name__)
app.register_blueprint(bp_tctdi)
conexaoBanco()

if __name__ == '__main__':
    app.run(debug=True)
