import psycopg2 as psycopg
import os
from dotenv import load_dotenv

load_dotenv()

host_name = os.environ.get("POSTGRES_HOST")
database_name = os.environ.get("POSTGRES_DB")
user_name = os.environ.get("POSTGRES_USER")
user_password = os.environ.get("POSTGRES_PASSWORD")

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
