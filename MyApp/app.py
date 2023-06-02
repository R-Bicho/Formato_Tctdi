from flask import Flask
from blueprints.webui import views

app = Flask(__name__, template_folder= "templates")
views.init_app(app)

app.run(debug=True)