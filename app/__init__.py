from flask import Flask, redirect
from flasgger import Swagger
from app.views.views import records
from app.views.user_views import user
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.register_blueprint(records)
app.register_blueprint(user)
jwt = JWTManager(app)
app.config['JWT_SECRET_KEY'] = 'lubwama'

# Define a swagger template
template = {
    "swagger": "2.0",
    "info": {
        "title":
        "Store Manager Application end-points",
        "description":
        "Store Manager is a web application that helps store owners manage and product inventory records.",
        "version":
        "v1"
    },
    "schemes": ["http", "https"]
}

# Instantiate swagger docs
swagger = Swagger(app, template=template)


@app.route('/')
def index():
    return redirect('/apidocs/')



