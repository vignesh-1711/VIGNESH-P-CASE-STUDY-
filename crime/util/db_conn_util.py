import pyodbc

class DBConnUtil:
    @staticmethod
    def get_connection():
        """Establishes a connection to the MS SQL Server database."""
        try:
            conn = pyodbc.connect('Driver={SQL Server};'
                                  'Server=LAPTOP-UB2OM4N3\SQLEXPRESS;'
                                  'Database=casestudy_crime_mgmt;'
                                  'Trusted_Connection=yes;')
            print("Connected Successfully")
            return conn
        except pyodbc.Error as e:
            print(f"Error connecting to database: {str(e)}")
            return None
