from flask import Flask, redirect
from flasgger import Swagger
from app.views.views import records
from app.views.user_views import user
from app.views.pro_views import product
from flask_jwt_extended import JWTManager
from app.views.sale_views import sale
from app.models.login import get_token
from app.views.category_views import category
import datetime

app = Flask(__name__)
app.register_blueprint(records)
app.register_blueprint(user)
app.register_blueprint(product)
app.register_blueprint(sale)
app.register_blueprint(category)
app.register_blueprint(get_token)
jwt = JWTManager(app)
app.config['JWT_SECRET_KEY'] = 'lubwama'
app.config['JWT_ACCESS_TIME_EXPIRES'] = datetime.timedelta(hours = 2)

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



