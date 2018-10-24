from flask import Flask, redirect
from flasgger import Swagger
from app.views.views import records

app = Flask(__name__)
app.register_blueprint(records)

# Define a swagger template
template = {
    "swagger": "2.0",
    "info": {
        "title":
        "Store Manager API",
        "description":
        "Store Manager is a web application that helps store owners manage\
         sales and product inventory records",
        "version":
        "1.0.0"
    },
    "schemes": ["http", "https"]
}

# Instantiate swagger docs
swagger = Swagger(app, template=template)


@app.route('/')
def index():
    return redirect('/apidocs/')
