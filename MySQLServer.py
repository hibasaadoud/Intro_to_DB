import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host="localhost",   # change if your server is remote
            user="root",        # replace with your MySQL username
            password=""         # replace with your MySQL password
        )

        # Only proceed if connection is successful
        if connection.is_connected():
            cursor = connection.cursor()
            # Create the database if it does not exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as db_err:
        # Catch MySQL-specific errors
        print(f"MySQL Error: {db_err}")

    except Exception as e:
        # Catch any other exceptions
        print(f"Error: {e}")

    finally:
        # Ensure cursor and connection are closed
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

# Entry point
if __name__ == "__main__":
    create_database()
