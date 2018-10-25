class Sales:
    def __init__(self, sale_id, prod_name, prod_quantity,
                 attendant, price):
        self.sale_id = sale_id
        self.prod_name = prod_name
        self.prod_quantity = prod_quantity
        self.price = price
        self.attendant = attendant
        


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


