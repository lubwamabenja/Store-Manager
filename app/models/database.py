import psycopg2
import uuid
import os
from werkzeug.security import generate_password_hash, check_password_hash

class MyDatabase():
    def __init__(self):
        try:
            if os.getenv('test_env') == 'testing':
                self.db = 'test_database'
            elif os.getenv('heroku_env') == 'heroku':
                self.db = os.getenv('DATABASE_URL')


            else:
                self.db = 'Store_db'
            connection = '''dbname={} user=lubwama password=lubwama1'''
            self.conn = psycopg2.connect(connection.format(self.db))
            self.cur = self.conn.cursor()
            self.conn.autocommit =True
            print(self.db)
        except Exception as e:
            print(e)
            print("Database connection failed")
                
    def create_users(self):
        self.cur.execute("\
        CREATE TABLE IF NOT EXISTS Users(user_id serial PRIMARY KEY,\
        username VARCHAR(60) NOT NULL UNIQUE,\
        password VARCHAR(100) NOT NULL,admin VARCHAR(30) )")
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
        attendant VARCHAR(20) NOT NULL,\
        FOREIGN KEY(prod_name) REFERENCES Products(prod_name),\
        date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")
        print("Sales table has been created")

    def create_categories(self):
        self.cur.execute("\
        CREATE TABLE IF NOT EXISTS Categories(category_id serial PRIMARY KEY,\
        category_name VARCHAR(50),\
        prod_name VARCHAR(50) )")
        print("Categories table has been created")

    

    def select(self, table, column, value):
        sql = """
        SELECT * FROM {} WHERE {}='{}'
        """.format(table, column, value)
        self.cur.execute(sql)
        record= self.cur.fetchone()
        return record

    def set_dafault_admin(self):
        password = generate_password_hash('lubwama1',method='sha256')
        username = 'lubwama'
        if not self.select('Users','username',username):
            self.cur.execute("\
            INSERT INTO Users(username,password,admin) VALUES(%s,%s,%s)",(username,password,'true'))
            print("Default admin is set")


        

    def select_id(self, table, column, value):
        sql = """
        SELECT * FROM {} WHERE {}= {}
        """.format(table, column, value)
        self.cur.execute(sql)
        record= self.cur.fetchone()

        return record


    def select_all(self,table):
        sql = '''SELECT * FROM {};'''.format(table)
        self.cur.execute(sql)
        records = self.cur.fetchall()
        return records


    def update(self,table,property,value1,column,value2):
        sql = '''UPDATE {} SET {} = '{}' WHERE {} = '{}';'''.format(table,property,value1,column,value2)
        self.cur.execute(sql)

    def delete(self, table, column, value):
        sql = """
        DELETE FROM {} WHERE {}='{}';
        """.format(table, column, value)
        self.cur.execute(sql)

    def delete_all(self,table,column,value):
        sql = '''DELETE  FROM {} WHERE {} = '{}';'''.format(table,column,value)
        self.cur.execute(sql)



