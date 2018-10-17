from flask import Flask,request,jsonify,json
from data_models import products,sales

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

    def get_sale(self):
        #check whether the id was provided in the URL
        if 'id' in request.args:
            id = int(request.args['id'])
        else:
            return "Error,No sale id field provided"
        #an empty list for our results
        results = []

        for sale in sales:
            if sale['sale_id']==id:
                results.append(sale)
        return jsonify(results)






