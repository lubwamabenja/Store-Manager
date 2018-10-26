# Store-Manager

Store Manager is a web application that helps store owners manage sales and product inventory records
* [![Coverage Status](https://coveralls.io/repos/github/lubwamabenja/Store-Manager/badge.svg?branch=challenge-2)](https://coveralls.io/github/lubwamabenja/Store-Manager?branch=challenge-2)
[![Build Status](https://travis-ci.org/lubwamabenja/Store-Manager.svg?branch=ft-add-product-161214893)](https://travis-ci.org/lubwamabenja/Store-Manager)<a href="https://codeclimate.com/github/lubwamabenja/Store-Manager/maintainability"><img src="https://api.codeclimate.com/v1/badges/b62d23c140bf51e17a9f/maintainability" /></a>[![Codacy Badge](https://api.codacy.com/project/badge/Grade/ea7bb4ded21d4c9bab090c9aa4ea0796)](https://www.codacy.com/app/lubwamabenja/Store-Manager?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=lubwamabenja/Store-Manager&amp;utm_campaign=Badge_Grade)[![codecov](https://codecov.io/gh/lubwamabenja/Store-Manager/branch/challenge-2/graph/badge.svg)](https://codecov.io/gh/lubwamabenja/Store-Manager)



## Installation
* run the following commands in  the terminal

This command downloads the repository on the local machin
```
git clone https://github.com/lubwamabenja/Store-Manager

```
Install the virtual environment inside the  repository

```
install virtual environmennt (virtualenv venv)

```
Activate  the virtual environment
```
activate by source venv/bin/activate
```
Install the requirements required to run the application
```
pip install -r requirements.txt
````
Start the Application
```
python run.py
```
Some of the end points cannot be accessed by normal users and hence they require logging in with the following details
Password = admin
Username = admin

## API Endpoints
 
 
| method |     Routes             |   Action                               |
| ------ | ---------------------- | -------------------------------------- | 
| GET    |  /v1/products          |	 Fetches all products                  |
| GET    |  /v1/sales	Fetches     |  all sales records                     |
| GET	   |  /v1/products/<prod_id>|	 Fetches a single product record by id |
| GET	   |  /v1/sales/<sale_id>	  |  Fetches a single sales record by id   |
| POST	 |    /v1/products	      |  Creates a product                     |
| POST	 |     /v1/sales	        |  Creates a sales order                 |
    
 * for POST request its better to use  POSTMAN
 
 
## UI(user interfaces)
* Below is the link to my user interfaces which are hosted on github
* https://lubwamabenja.github.io/Store-Manager/
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


