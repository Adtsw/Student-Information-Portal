import mysql.connector
from mysql.connector import Error

class DBManager:
    def __init__(self, host='localhost', user='root', password='', database='StudentInfoPortal'):
        try:
            print("Connecting to Database...")
            self.connection = mysql.connector.connect(
                user= user,
                password= password,
                host= host,
                database= database
            )
            print("Connected to Database.")
            self.connection.autocommit = False
        except Error as e:
            print(f"Error connecting to database: {e}")
            raise
        
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            self.connection.rollback()
        else:
            self.connection.commit()
            self.close()
            
    def close(self):
        if self.connection and self.connection.is_connected():
            print("Still Connected to Database.")
            print("Closing Database Connection...")
            self.connection.close()
        else:
            print("Connection is already closed.")
            
    def execute(self, query, params=None):
        cursor = self.connection.cursor(dictionary=True)
        cursor.execute(query, params or ())
        return cursor
    
    def executeCommand(self, query, params=None, type='commit'):
        try:
            with self.connection.cursor(dictionary=True, buffered=True) as cursor: # automatically closes the cursor under finally block with cursor.close()
                cursor.execute(query, params or ())
        
            if type == 'fetchone':
                return cursor.fetchone()
            elif type == 'fetchall':
                return cursor.fetchall()
            else:
                self.connection.commit()
                return cursor.lastrowid
            
        except Error as e:
            print(f"Databse error: {e}")
            raise 