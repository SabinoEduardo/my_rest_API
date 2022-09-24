import pymysql.cursors
from scraping import Date
from datetime import datetime
from contextlib import contextmanager


@contextmanager
def conect_db():
    """
        Connect to the Database
    """
    conexao = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='',
        db='DB_product_Scraping',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        yield conexao
    finally:
        conexao.close()


def insert_into(products):
    """
    This Function is used to insert the products to the Database
    :param products: instance of class Dates
    :return: funtion without return
    """
    for id_product, prod in products.items():
        try:
            sql = 'INSERT INTO open_food_product (code, barcode, status, imported_t, url, product_name, ' \
                  'quantity, categories, packaging, brands, image_url) ' \
                  'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'

            cursor.execute(
                            sql, (prod['code'], prod['barcode'], 'imported', f'{datetime.now()}',
                                  prod['url'], prod['product_name'], prod['quantity'],
                                  prod['categories'], prod['packaging'], prod['brands'],
                                  prod['image_url'])
                        )

            con.commit()
        except pymysql.err.IntegrityError:
            pass


with conect_db() as con:  # To call the function connect_db to open the connection with database
    with con.cursor() as cursor:  # To start the cursor
        cursor.execute('SELECT * FROM open_food_product')  # To get all products of database
        quantity_of_product = len(cursor.fetchall())  # To calculate how much products exist in database
        page_site = int(quantity_of_product/100) + 1
        product = Date(page_site)
        insert_into(product.products())
