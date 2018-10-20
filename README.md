# Store-Manager

Store Manager is a web application that helps store owners manage sales and product inventory records
* [[![Coverage Status](https://coveralls.io/repos/github/lubwamabenja/Store-Manager/badge.svg?branch=features)](https://coveralls.io/github/lubwamabenja/Store-Manager?branch=features)
[![Build Status](https://travis-ci.org/lubwamabenja/Store-Manager.svg?branch=ft-add-product-161214893)](https://travis-ci.org/lubwamabenja/Store-Manager)<a href="https://codeclimate.com/github/lubwamabenja/Store-Manager/maintainability"><img src="https://api.codeclimate.com/v1/badges/b62d23c140bf51e17a9f/maintainability" /></a>

## Installation
* run the following commands
```
git clone https://github.com/lubwamabenja/Store-Manager
install virtual environmennt (virtualenv venv)
activate by source venv/bin/activate
pip install -r requirements.txt
python run.py

Password = admin
Username = admin

```
## API Endpoints
	
* GET         /v1/products      	 Fetches all products
* GET         /v1/sales	Fetches          all sales records
* GET	      /v1/products/<prod_id>	 Fetches a single product record by id
* GET	      /v1/sales/<sale_id>	 Fetches a single sales record by id
* POST	      /v1/products	         Creates a product
* POST	      /v1/sales	                 Creates a sales order
    
 * for POST request its better to use  POSTMAN
 
 
 



## Getting started with github pages 
* git clone https://github.com/lubwamabenja/Store-Manager.git
* username: lubwama
* password: lubwama1
### Description
```
Store attendant can search and add products to buyer’s cart.
Store attendant can see his/her sale records but can’t modify them.
App should show available products, quantity and price.
Store owner can see sales and can filter by attendants.
Store owner can add, modify and delete products.


```

## Built With

* Flask- The web framework used for API's
* JPython,Postgresql - Dependency Management
* Html,javascript,Css  - UI Templates



## Authors

Lubwama Isaac

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* ANDELA TECHNOLOGIES


