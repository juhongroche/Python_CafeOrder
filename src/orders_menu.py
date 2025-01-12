from read_data import read_orders_data, load_menu_options, read_couriers_data, read_products_data
from connect_database import *


# Adding orders
def add_new_order():

    sql= """
        INSERT INTO orders (customer_name, customer_address, customer_phone, product_id, courier_id, order_status)
        VALUES (%s,%s,%s,%s,%s,%s)
        """
    
    # Getting user input for new order
    customer_name_input = input('Enter customer name: ')
    customer_addr_input = input('Enter customer address: ')
    customer_phone_input = input('Enter customer phone number: ')
    
    read_products_data()

    try:
        # Allow user to add multiple products
        product_ids = []
        while True:
            product_id = int(input('Enter product ID (or 0 to stop): '))
            if product_id == 0:
                break   # Exit the loop when user enters '0'
            cursor.execute('SELECT * FROM products WHERE product_id =%s',(product_id,))
            current_product = cursor.fetchone()
            if current_product is None:
                print(f'Product ID {product_id} not found. Try again!')
            else:
                product_ids.append (product_id)      
    except (ValueError, TypeError) as error:
        print(f'Error: {error}. Enter a valid ID number')
        return
    except (Exception) as error:
        print(f'Unexpected error: {error}')
        return
    
    if not product_ids:
        print('No valid products selected. Try again!')

    read_couriers_data()
    try:
        courier_id = int(input('Enter courier ID: '))
        cursor.execute('SELECT * FROM couriers WHERE courier_id =%s',(courier_id,))
        current_courier = cursor.fetchone()
        if current_courier is None:
            print(f'Courier ID {courier_id} not found.')
            return       
    except (ValueError, TypeError) as error:
        print(f'Error: {error}. Enter a valid ID number')
        return
    except (Exception) as error:
        print(f'Unexpected error: {error}')
        return

    order_status = 1  # PREPARING by default

    try:
        # Using a loop to insert each product ID in the products table
        for product_id in product_ids:
            data_value = (customer_name_input,customer_addr_input,customer_phone_input,product_id,courier_id,order_status)
            cursor.execute(sql,data_value)
    
        connection.commit()

        print(f'New order created for {customer_name_input}')

    except Exception as e:
        connection.rollback()  # Rollback in case of an error
        print(f'Error: {e}. Try again!')


# creating a function to update order status
def update_order_status():
    read_orders_data()

    try:
        order_id = int(input('Enter order ID to update the order status: '))
        cursor.execute('SELECT * FROM orders WHERE order_id =%s',(order_id,))
        current_order = cursor.fetchone()
        if current_order is None:
            print(f'Courier ID {order_id} not found.')
            return       
    except (ValueError, TypeError) as error:
        print(f'Error: {error}. Enter a valid ID number')
        return
    except (Exception) as error:
        print(f'Unexpected error: {error}')
        return

    else: 
        # Print order status option
        load_menu_options('order-status.txt')
        new_status = int(input('Enter new order status ID: '))
        update_sql = 'UPDATE orders SET order_status = %s WHERE order_id =%s'
        cursor.execute(update_sql, (new_status,order_id))
        connection.commit()
        print(f'ID: {order_id} order status has been updated to {new_status}')


# Updating existing order
def update_order():
    read_orders_data()
    try:
        order_id = int(input('Enter order ID to update the order status: '))
        cursor.execute('SELECT * FROM orders WHERE order_id =%s',(order_id,))
        current_order = cursor.fetchone()
        if current_order is None:
            print(f'Courier ID {order_id} not found.')
            return       
    except (ValueError, TypeError) as error:
        print(f'Error: {error}. Enter a valid ID number')
        return
    except (Exception) as error:
        print(f'Unexpected error: {error}')
        return

    else: 
        print('Enter new details below. (or press ENTER to keep current values)')
        new_customer_name = input(f'Enter new customer name (current: {current_order[1]}): ') or current_order[1]
        new_customer_address = input(f'Enter new customer address (current: {current_order[2]}): ') or current_order[2]
        new_customer_phone = input(f'Enter new customer phone number (current: {current_order[3]}): ') or current_order[3]

            
        try:
            new_product_id = int(input(f'Enter new product ID (current: {current_order[4]}): ')) or current_order[4]           
            cursor.execute('SELECT * FROM products WHERE product_id =%s',(new_product_id,))
            current_product = cursor.fetchone()
            if current_product is None:
                print(f'Product ID {new_product_id} not found.')
                return       
        except (ValueError, TypeError) as error:
            print(f'Error: {error}. Enter a valid ID number')
            return
        except (Exception) as error:
            print(f'Unexpected error: {error}')
            return

        try:
            new_courier_id = int(input(f'Enter new courier ID (current: {current_order[5]}): ')) or current_order[5]
            cursor.execute('SELECT * FROM couriers WHERE courier_id =%s',(new_courier_id,))
            current_courier = cursor.fetchone()
            if current_courier is None:
                print(f'Courier ID {new_courier_id} not found.')
                return  
        except (ValueError, TypeError) as error:
            print(f'Error: {error}. Enter a valid ID number')
            return
        except (Exception) as error:
            print(f'Unexpected error: {error}')
            return

        try: 
            new_order_status = int(input(f'Enter order ID to update (current: {current_order[6]}): ')) or current_order[6]
            cursor.execute('SELECT * FROM order_status WHERE id =%s',(new_order_status,))
            current_order_status = cursor.fetchone()
            if current_order_status is None:
                print(f'Order Status ID {new_order_status} not found.')
                return  
        except (ValueError, TypeError) as error:
            print(f'Error: {error}. Enter a valid ID number')
            return
        except (Exception) as error:
            print(f'Unexpected error: {error}')
            return          

        else:
            update_sql = 'UPDATE orders SET customer_name =%s, customer_address=%s, customer_phone=%s, product_id=%s, courier_id=%s, order_status=%s WHERE order_id=%s'
            cursor.execute(update_sql, (new_customer_name, new_customer_address,new_customer_phone, new_product_id, new_courier_id, new_order_status, order_id))

            connection.commit()
            print(f'ID: {order_id} has been updated')


# Deleting Order
def delete_order():
    read_orders_data()

    try:
        order_id = int(input('Enter order ID to delete: '))
        cursor.execute(f'SELECT * FROM orders WHERE order_id = {order_id}')
        current_order = cursor.fetchone()

        if current_order is None:
            print(f'Order ID: {order_id} not found.')
            return
    
    except (ValueError, TypeError) as error:
        print(f'Error: {error}. Enter a valid ID number')
        return
    except (Exception) as error:
        print(f'Unexpected error: {error}')
        return
    
    else:
        sql_command = 'DELETE FROM orders WHERE order_id = %s'
        cursor.execute(sql_command, (order_id,))
        connection.commit()
        print(f'ID:{order_id} order has been deleted.')



# creating a main function for orders menu
def orders_menu():
    
    while True:
        load_menu_options('orders-menu-options.txt')
        # raising index error for wrong user input
        try:
            # Get user input for the order menu option
            orders_menu_input = int(input("Please choose your option: "))
            if orders_menu_input <0 or orders_menu_input >5:
                raise IndexError('Invalid option. (0,1,2,3,4,5)')
        except (IndexError, ValueError) as error:
            print(f'Error: {error}')
            print('Invalid option! Enter a valid option. (0,1,2,3,4,5)')
        
        else:
            if orders_menu_input == 0:
                from app import main_menu
                return main_menu()
           
            elif orders_menu_input == 1:
                read_orders_data()

            elif orders_menu_input == 2:
                add_new_order()
        
            elif orders_menu_input == 3:
                update_order_status()
            
            elif orders_menu_input == 4:
                update_order()

            elif orders_menu_input == 5:
                delete_order()
