import psycopg2 as psycopg

host_name = 'localhost'
database_name = 'test'
user_name = 'postgres'
user_password = 'mysecretpassword'

try:
# Establish a database connection
    with psycopg.connect(f"""
        host={host_name}
        dbname={database_name}
        user={user_name}
        password={user_password}
        """) as connection:
        cursor = connection.cursor()
except Exception as ex:
    print('Failed to: ', ex)



def append_database(product_input, price_input):
    sql = """
        INSERT INTO products (product, price)
        VALUES (%s,%s)        
    """
    data_values = (product_input, price_input)

    cursor.execute(sql, data_values)
    connection.commit()

def add_new_products():
    product_input = input('Enter your product: ')
    price_input = float(input('Enter price: '))

    return append_database(product_input, price_input)


def test_add_new_product():
    # Arrange
    product_input = 'apple'
    price_input = 0.5
    expected = append_database('apple', 0.5)


    # Act
    result = append_database(product_input, price_input)

    # Assert
    assert result == expected

test_add_new_product()