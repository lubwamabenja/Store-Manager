class Products:

    def __init__(self, prod_id, prod_name, prod_category,
                 prod_quantity, unit_cost):
        self.prod_id = prod_id
        self.prod_name = prod_name
        self.prod_category = prod_category
        self.prod_quantity = prod_quantity
        self.unit_cost = unit_cost


    def get_records(self):
        dict = {
            "prod_id": self.prod_id,
            "prod_name": self.prod_name,
            "prod_category": self.prod_category,
            "prod_quantity": self.prod_quantity,
            "unit_cost": self.unit_cost
        }
        return dict
        



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

