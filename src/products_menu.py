from read_data import read_products_data, load_menu_options
from connect_database import *

# Fetches a product by its ID from the database
def fetch_product_by_id(product_id):
    cursor.execute(f'SELECT * FROM products WHERE product_id ={product_id}')
    return cursor.fetchone()


def add_new_product():

    sql = """
        INSERT INTO products (product, price)
        VALUES (%s,%s)        
    """
    product_input = input('Enter product name: ')
    if product_input =='':
        print('Invalid input. Try again!')
        return

    try:
        price_input = float(input('Enter price(£): '))
    except (ValueError, TypeError) as error:
        print(f'{error}. Invalid input entered. Please enter a valid input.')
        return

    data_values = (product_input, price_input)

    cursor.execute(sql, data_values)
    connection.commit()

    print(f'{product_input}: £{price_input} has been added.')
    

# Updating existing products in the list
def update_products():
    read_products_data()

    try:
        product_id = int(input('Enter product ID to update: '))
        cursor.execute(f'SELECT * FROM products WHERE product_id = {product_id}')
        current_data = cursor.fetchone()
        # raising error for wrong user input
        if current_data is None:
            print(f'Product ID {product_id} not found.')
            return
        
    except (ValueError, TypeError) as error:
        print(f'Error: {error}. Enter a valid product ID')
        return
    except (Exception) as error:
        print(f'Unexpected error: {error}')
        return

    else:
        print('Enter new details below. (or press ENTER to keep current values)')

        new_product = input(f'Enter new product name (current: {current_data[1]}): ')
        new_price = input(f'Enter new price(£) (current: £{current_data[2]}): ')

        if new_product=='':
            new_product = current_data[1]
        if new_price =='':
            new_price = current_data[2]
            
        else:
            try:
                new_price = float(new_price)
            except ValueError:
                print('Invalid price entered. Price must be a number.')
                return
        
        update_sql = 'UPDATE products SET product = %s, price = %s WHERE product_id = %s'
        cursor.execute(update_sql, (new_product,new_price,product_id))

        connection.commit()
        print(f'ID: {product_id} has been updated to "{new_product}" with price: £{new_price}')



# Deleting product
def delete_product():
    read_products_data()

    try:
        product_id = int(input('Enter product ID to delete: '))
        row_to_delete = fetch_product_by_id(product_id)

        if row_to_delete == None:
            print(f'Product ID: {product_id} not found.')
            return
        
    except (ValueError, TypeError) as error:
        print(f'Error: {error}. Enter a valid product ID')
        return
    except (Exception) as error:
        print(f'Unexpected error: {error}')
        return

    else:
        sql_command ='DELETE FROM products WHERE product_id = %s'

        cursor.execute(sql_command, (product_id,))
        connection.commit()
        print(f'Product ID {product_id}: {row_to_delete[1]} has been deleted.')

    
    


# creating a function for products menu    
def products_menu():

    while True:
        # display_products_menu_options
        load_menu_options('products-menu-options.txt')

    # raising index error for wrong user input
        try:
            # Get user input for the product menu option
            products_menu_input = int(input('Please choose your option: '))
            if products_menu_input <0 or products_menu_input > 4:
                raise IndexError('Index error')
        except (IndexError, ValueError) as error:
            print(f'Error: {error}')
            print('Invalid option! Enter a valid option. (0,1,2,3,4)')

        else:
            if products_menu_input == 0:
                from app import main_menu
                return main_menu()      

            elif products_menu_input == 1:
                read_products_data()

            elif products_menu_input == 2:
                add_new_product()

            elif products_menu_input == 3:
                update_products()           

            elif products_menu_input == 4:
                delete_product()
