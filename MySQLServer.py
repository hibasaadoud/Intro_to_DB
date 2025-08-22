
import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server (replace user/password if needed)
        connection = mysql.connector.connect(
            host="localhost",   # change if your server is remote
            user="root",        # replace with your MySQL username
            password=""         # replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Create database if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        # Print any error while connecting or creating the database
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # Always close cursor and connection
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

# Entry point
if __name__ == "__main__":
    create_database()
