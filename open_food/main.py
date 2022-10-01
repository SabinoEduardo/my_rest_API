from open_food.sync_products import (conect_db, log_txt)


with conect_db() as con:  # To call the function connect_db to open the connection with database
    with con.cursor() as cursor:  # To start the cursor
        cursor.execute('SELECT * FROM open_food_product')  # To get all products of database
        quantity_of_product_in_db = len(cursor.fetchall())  # To calculate how much products exist in database
        number_page = int(quantity_of_product_in_db/100) + 1
        log_txt(number_page, con, cursor)
