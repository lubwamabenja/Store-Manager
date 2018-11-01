import psycopg2
import uuid
import os
from werkzeug.security import generate_password_hash, check_password_hash

class MyDatabase():
    def __init__(self):
        try:
            if os.getenv('APP_SETTINGS') == 'testing':
                self.db = 'test_database'
            else:
                self.db = 'Store_db'
            self.conn =  psycopg2.connect("dbname=Store_db user=lubwama password=lubwama1")
            self.cur = self.conn.cursor()
            self.conn.autocommit =True
        except:
            print("Database connection failed")
                
    def create_users(self):
        self.cur.execute("\
        CREATE TABLE IF NOT EXISTS Users(user_id serial PRIMARY KEY,\
        username VARCHAR(60) NOT NULL UNIQUE,\
        password VARCHAR(100) NOT NULL,admin BOOL NOT NULL )")
        print('User Table has been created successfully')
    
    def create_products(self):
        self.cur.execute("\
        CREATE TABLE IF NOT EXISTS Products(prod_id serial PRIMARY KEY,\
        prod_name VARCHAR(60) NOT NULL UNIQUE,prod_quantity INTEGER NOT NULL,\
        unit_cost INTEGER NOT NULL,\
        category_name VARCHAR(50), \
        date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")
        print("Products table has been created")

    def create_sales(self):
        self.cur.execute("\
        CREATE TABLE IF NOT EXISTS Sales(sale_id serial PRIMARY KEY,\
        prod_name VARCHAR(50) NOT NULL ,\
        prod_quantity INTEGER NOT NULL,\
        FOREIGN KEY(prod_name) REFERENCES Products(prod_name),\
        date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")
        print("Sales table has been created")

    def create_categories(self):
        self.cur.execute("\
        CREATE TABLE IF NOT EXISTS Categories(category_id serial PRIMARY KEY,\
        category_name VARCHAR(50),\
        prod_name VARCHAR(50) )")
        print("Categories table has been created")

    def set_dafault_admin(self):
        password = generate_password_hash('lubwama1',method='sha256')
        self.cur.execute("\
        INSERT INTO Users(username,password,admin) VALUES(%s,%s,%s)",('lubwama',password,True))
        print("Default admin is set")
      
        
      
        

if __name__ == '__main__':
    db = MyDatabase()
    db.create_products()
    db.create_users()
    db.create_categories()
    db.create_sales()
    db.set_dafault_admin()
