from flask import Flask
from blueprints.views import bp_tctdi
from blueprints.views_login import bp_login

app = Flask(__name__)
app.register_blueprint(bp_login)
app.register_blueprint(bp_tctdi)

if __name__ == '__main__':
    app.run(debug=True)
