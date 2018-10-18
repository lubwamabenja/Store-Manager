from flask import Flask,request,jsonify,json
from data_models import products,sales

class Products:
    def add_products(self):
        prod_data = json.loads(request.data.decode('utf-8'))
        product = {
            'prod_id':prod_data['prod_id'],
            'prod_name':prod_data['prod_name'],
            'prod_category':prod_data['prod_category'],
            'prod_quantity': prod_data['prod_quantity'],
            'unit_cost': prod_data['unit_cost']
        }
        products.append(product)
        return jsonify(products)

class Sales:
    """ class contains sales functions """
    
    def add_sales(self):
        ''' function adds sale records to store '''
        req_data = json.loads(request.data.decode('utf-8'))
        sale_order = {
            'sale_id':req_data['sale_id'],
            'prod_name':req_data['prod_name'],
            'prod_quantity':req_data['prod_quantity'],
            'attendant':req_data['attendant'],
            'price':req_data['price']}
        sales.append(sale_order)
        sales.append(sale_order)
        return jsonify(sales)

    