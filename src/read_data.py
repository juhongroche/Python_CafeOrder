from connect_database import *

def read_products_data():    
    cursor.execute('SELECT * FROM products')
    rows = cursor.fetchall()
    connection.commit()
    for row in rows:
        print(f'Product ID: {row[0]} | Product: {row[1]} | Price: £{row[2]}')

def read_couriers_data():
    cursor.execute('SELECT * FROM couriers')
    rows = cursor.fetchall()
    connection.commit()
    for row in rows:
        print(f'Courier ID: {row[0]} | Courier Name: {row[1]} | Phone Number: {row[2]}')

def read_orders_data():
    cursor.execute('SELECT * FROM orders')
    rows = cursor.fetchall()
    connection.commit()
    for row in rows:
        print(f'Order ID: {row[0]} | Customer Name: {row[1]} | Customer Address: {row[2]} | Phone Number: {row[3]} | Product ID: {row[4]} |  Courier ID: {row[5]} | Order Status: {row[6]}')


def load_menu_options(menu_option_file):
    try:
        with open(menu_option_file,'r') as file:
            menu=file.read()
            print(menu)
    except Exception as error:
        print(f'File does not exist!: {error}')


