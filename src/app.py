from products_menu import products_menu
from orders_menu import orders_menu
from couriers_menu import couriers_menu
from read_data import load_menu_options
import psycopg2 as psycopg
import os
from dotenv import load_dotenv
from connect_database import *



def main_menu():

    while(True):   
        load_menu_options('main-menu-options.txt')
        try:
            main_menu_input = int(input("Please enter your option (0,1,2,3): "))

        # raising index error for wrong user input
            if main_menu_input<0 or main_menu_input >= 4:
                raise ValueError('Invalid Option!')
            
        except (ValueError) as error:
            print(f'Error: {error}.')
            print('Enter a valid option (0,1,2,3).')
            continue
        
        else:
            if main_menu_input == 0:
                exit()
            
            elif main_menu_input == 1:
                products_menu()

            elif main_menu_input == 2:
                couriers_menu()

            elif main_menu_input == 3:
                orders_menu()

main_menu()
