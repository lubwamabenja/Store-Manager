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

    def get_product(self):
        '''check whether the id was provided in the URL '''
        if 'id' in request.args:
            id = int(request.args['id'])
        else:
            return "Error,No id field provided"
        #an empty list for our results
        results = []

        for product in products:
            if product['prod_id']==id:
                results.append(product)
        return jsonify(results)
