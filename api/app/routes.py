from flask import Flask,request,jsonify,json
from data_models import products,sales
from sales import *
from products import *
from errors import *

app = Flask(__name__)


sales_data = Sales()
product_data = Products()



@app.route('/',methods=['GET'])
def index():
    return "<h1>Store Manager</h1> <p>Welcome to my app</p>"


@app.route('/v1/products',methods=['GET'])
def api_all():
    return jsonify(products)

@app.route('/v1/products/ids',methods=['GET'])
def get_product():
    return product_data.get_product()

 
""" This route enables attendant/owner to add products """
@app.route('/v1/products',methods=['POST'])
def add_product():
    return product_data.add_products()

''' this route returns all the sales records made  by the attendant '''
@app.route('/v1/sales',methods=['GET'])
def get_sales():
    return jsonify(sales)


@app.route('/v1/sales/ids',methods=['GET'])
def get_sale():
    return sales_data.get_sale()


#This route enables attendant/owner to add sales
@app.route('/v1/sales',methods=['POST'])
def add_sales():
    return sales_data.add_sales()
    

#runs the app
if __name__==('__main__'):
    app.run(port=8080 ,debug=True)