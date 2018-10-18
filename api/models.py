from flask import Flask,request,jsonify,json

""" this is the list of all products available in the store """
products = [
    {
        'prod_id' : 0,
        'prod_name':'crisps',
        'prod_category':'snacks',
        'prod_quantity':'4 cartons',
        'unit_cost':500
    },
    {
        'prod_id': 1,
        'prod_name':'ethernet',
        'prod_category':'cables',
        'prod_quantity':'8 cables',
        'unit_cost': 10000
    }
]

""" this is a list of all sale records """
sales = [
    {
        'sale_id': 0,
        'prod_name': 'crisps',
        'prod_quantity':'5 pkts',
        'price': 2500,
        'attendant':'john'
    },
    {
        'sale_id': 1,
        'prod_name': 'ethernet',
        'prod_quantity':'1 m',
        'price':10000,
        'attendant':'peter'

    }
]



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

    