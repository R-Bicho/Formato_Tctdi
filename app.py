from flask import Flask
from blueprints.views import bp_tctdi

app = Flask(__name__)
app.register_blueprint(bp_tctdi)

app.run(debug=True)