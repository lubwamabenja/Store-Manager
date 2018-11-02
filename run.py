from app import app
from app.models.database import *


if __name__ == '__main__':
	db = MyDatabase()
	db.create_products()
	db.create_users()
	db.create_categories()
	db.create_sales()
	db.set_dafault_admin()
	app.run(debug=8080)
