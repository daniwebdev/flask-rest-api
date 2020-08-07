from flask import Flask, request

app = Flask(__name__)
# Load Config
app.config.from_object('config')

from app.modules.auth.controller import auth_module
from app.modules import register

# Module Register
for reg_module in register:
    app.register_blueprint(reg_module)


@app.route('/')
def home():
    return ".::'''''''' HALO ''''''''::. "
