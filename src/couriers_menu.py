from read_data import load_menu_options, read_couriers_data
from connect_database import *


# Adding courier
def add_new_courier():

    sql = """
        INSERT INTO couriers (courier_name, courier_phone)
        VALUES (%s,%s)
        """
       
    # Getting user input for new courier
    name_input = input('Enter courier name: ')
    if name_input =='':
        print('Invalid input. Try again!')
        return
    phone_input = input('Enter courier phone number: ')
    if phone_input=='':
        print('Invalid input. Try again!')
        return


    else:
        data_values = (name_input, phone_input)
        
        cursor.execute(sql, data_values)
        connection.commit()

        print(f'{name_input}: {phone_input} has been added.')


# Update existing courier :TBC
def update_courier():
    read_couriers_data()

    try:    
        courier_id = int(input('Enter courier ID to update: '))
        cursor.execute('SELECT * FROM couriers WHERE courier_id = %s', (courier_id,))
        current_data = cursor.fetchone()
        if current_data is None:
            print(f'Courier ID {courier_id} not found.')
            return

    except (ValueError, TypeError) as error:
        print(f'Error: {error}. Enter a valid ID number')
        return
    except (Exception) as error:
        print(f'Unexpected error: {error}')
        return
    
    else:
        print('Enter new details below. (or press ENTER to keep current values)')

        new_courier = input(f'Enter new courier name (current: {current_data[1]}): ')
        new_phone = input(f'Enter new courier phone number (current: {current_data[2]}): ')
        
        if new_courier=='':
            new_courier = current_data[1]
        if new_phone=='':
            new_phone = current_data[2]
        
        update_sql = 'UPDATE couriers SET courier_name = %s, courier_phone = %s WHERE courier_id = %s'
        cursor.execute(update_sql, (new_courier, new_phone, courier_id))

        connection.commit()
        print(f'ID: {courier_id} has been updated to "{new_courier}" : "{new_phone}".')
       

# Deleting courier
def delete_courier():
    read_couriers_data()

    try:    
        courier_id = int(input('Enter courier ID to delete: '))
        cursor.execute(f'SELECT * FROM couriers WHERE courier_id ={courier_id}')
        current_data = cursor.fetchone()
        
        if current_data == None:
            print(f'Courier ID: {courier_id} not found.')
            return

    except (ValueError, TypeError) as error:
        print(f'Error: {error}. Enter a valid ID number')
        return
    except (Exception) as error:
        print(f'Unexpected error: {error}')
        return
    
    else:
        sql_command = 'DELETE FROM couriers WHERE courier_id = %s'
        cursor.execute(sql_command, (courier_id,))
        connection.commit()
        print(f'{current_data} has been deleted.')
    


# Creatig a main function for couriers menu
def couriers_menu():

    while True:
        # displaying menu option
        load_menu_options('couriers-menu-options.txt')

        # raising index error for wrong user input
        try:
            # Get user input for the product menu option
            couriers_menu_input = int(input('Please choose your option: '))
            if couriers_menu_input <0 or couriers_menu_input > 4:
                raise IndexError('Index error')
        except (IndexError, ValueError) as error:
            print(f'Error: {error}')
            print('Invalid option! Enter a valid option. (0,1,2,3,4)')

        else:
            # Get user input for the courier menu option
            if couriers_menu_input == 0:
                from app import main_menu
                return main_menu()
            
            elif couriers_menu_input == 1:
                read_couriers_data()

            elif couriers_menu_input == 2:
                add_new_courier()

            elif couriers_menu_input == 3:
                update_courier()
            
            elif couriers_menu_input == 4:
                delete_courier()
            

