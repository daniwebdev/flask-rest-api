from flask import Flask
from app.modules.auth.controller import auth_module
app = Flask(__name__)

app.config.from_object('config')

app.register_blueprint(auth_module)

@app.route('/')
def home():
    return ".::'''''''' HALO ''''''''::. "