import pymysql.cursors
from scraping import Dados
from datetime import datetime
from contextlib import contextmanager


@contextmanager
def conect_db():
    conexao = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='',
        db='DB_product_scraping',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        yield conexao
    finally:
        conexao.close()


products = Dados()
p = products.products()


with conect_db() as con:
    for id_product, product in products.products().items():
        print(product['packaging'])
        with con.cursor() as cursor:
            sql = 'INSERT INTO open_food_produto (code, barcode, status, imported_t, url, product_name, quantity, ' \
                 'categories, packaging, brands, image_url) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'

            cursor.execute(
                            sql, (product['code'], product['barcode'], 'imported', f'{datetime.now()}',
                                  product['url'], product['product_name'], product['quantity'], product['categories'],
                                  product['packaging'], product['brands'], product['image_url'])
                        )

            con.commit()
