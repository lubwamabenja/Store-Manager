from flask import Flask,request,json,jsonify
class Sales:
    """ class contains sales functions """
    def __init__(self, sale_id, prod_name, prod_quantity,
                 attendant, price):
        self.sale_id = sale_id
        self.prod_name = prod_name
        self.prod_quantity = prod_quantity
        self.attendant = attendant
        self.price = price
       
    
    def add_sales(self):
        ''' function adds sale records to store '''
        req_data = json.loads(request.data.decode('utf-8'))
        sale_order = {
            'sale_id':req_data['self.sale_id'],
            'prod_name':req_data['self.prod_name'],
            'prod_quantity':req_data['self.prod_quantity'],
            'attendant':req_data['self.attendant'],
            'price':req_data['self.price']}
        sales.append(sale_order)
        return jsonify(sales)

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


