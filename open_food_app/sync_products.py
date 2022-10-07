from scraping import Date
from datetime import datetime
import pymysql.cursors
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


def insert_into(products, con, cursor) -> bool:
    """
    This Function is used to insert the products to the Database
    :param con:
    :param cursor:
    :param products: instance of class Dates
    :return: funtion without return
    """
    try:
        for id_product, prod in products.items():
            try:
                sql = 'INSERT INTO open_food_product (code, barcode, status, imported_t, url, product_name, ' \
                      'quantity, categories, packaging, brands, image_url) ' \
                      'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'

                import_t = datetime.now()
                cursor.execute(
                                sql, (prod['code'], prod['barcode'], 'imported', f'{import_t}',
                                      prod['url'], prod['product_name'], prod['quantity'],
                                      prod['categories'], prod['packaging'], prod['brands'],
                                      prod['image_url'])
                            )
                con.commit()

            except pymysql.err.IntegrityError as error:
                with open('log.txt', 'a') as file:
                    file.write(f'{str(error)}\n')
                    return False
        return True
    except AttributeError as error:
        with open('log.txt', 'a') as f:
            f.write(f'{str(error)}\n')
            f.write('\n')
            return False


def log_txt(number_sync, con, cursor):
    with open('log.txt', 'a') as f:
        time1 = datetime.now().minute
        quantity_of_product_to_scraping = 100
        product = Date(number_sync, quantity_of_product_to_scraping)
        insert = insert_into(product.products(), con, cursor)
        if insert:
            time2 = datetime.now().minute
            date = datetime.now().strftime('%Y/%m/%d %I:%M:%S %p')
            time = time2 - time1
            f.write(f'Synchronization number: {number_sync}\n')
            f.write(f'  Sincronização realizada com sucesso!\n')
            f.write(f'  Synchronization Date: {date}\n')
            f.write(f'  The sync lasted {time} minutes\n')
            f.write('\n')
            f.seek(0)
        else:
            return
