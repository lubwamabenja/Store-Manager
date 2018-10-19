from flask import Flask,request,json,jsonify
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

