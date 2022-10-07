# Backend Challenge 20220626

## Product Scraping - Objective
Develop a REST API that will use data from Open Food Facts, an open database with nutritional information for various products.

### Languages, Frameworks and Libraries used
- Python
- Django
- Djangorestframework
- Pymysql
- Requests
- BeautifulSoup
- mysql-client

### The project
This project consists of a Mysql database and an update system.

The update system performs a daily scraping of the page [Open Food Facts](https://world.openfoodfacts.org/) and syncs this information to the database.

### Run the program

Functions were written in python to test the 3 API endpoints.

All tests were done in a development environment.

To run the program it is necessary to have pycharm or Vscode and Ptyhon3 installed on the machine. All libraries are stored in the virtual environment, so it is not necessary to install them again.

The requirements.txt file has all the libraries used in project development.

The main focus in building the program was the backend.

To update (synchronize) the products in the database it is necessary to run the main.py file. Before running, make sure that the virtual environment is active and that the server is connected.

In development, wampserver was used as a server to connect the database.

To view product information in the API, follow these steps:
- Run in the terminal the following line in the terminal: py manage.py runserver
- Access the service at http://127.0.0.1:8000/
- Display pages according to endpoints

The endpoints are:
- `GET /`: Return a Status: 200 and a Message "Fullstack Challenge 20201026"
- `GET /products/:code`: Get information for only one product;
- `GET /products`: List all products in the database, use the paging system to not overload `REQUEST`.
- `GET /documentations`: Documentation page.

The Pagination system was used to display 10 products per page in the API interface. To display other pages, enter the following path: http://127.0.0.1:8000/products/?page=numero_da_pagina

Page number takes an integer numeric value.

## Project presentation video
https://www.loom.com/share/2b451ce5536b438f8429a74f23bc6872
