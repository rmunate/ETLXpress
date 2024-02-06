#---------------------------------------------------------#
# Update Script Path                                      #
#---------------------------------------------------------#

from os.path import abspath, join, dirname
import sys

project_directory = abspath(join(dirname(__file__), '../../'))
if project_directory not in sys.path:
    sys.path.insert(0, project_directory)

#---------------------------------------------------------#
# Singleton Class for Oracle Database Connection          #
# Last Modification: 05-02-2024                           #
# Developers:                                             #
# -------------    Raul Mauricio Uñate Castro             #
#---------------------------------------------------------#

# Module Imports
from core.Clarity.Logger import Logger
import cx_Oracle

# Oracle Connection Class
class Oracle:

    # Singleton instance for connection.
    _instance = None
    
    # Class initialization.
    def __init__(self, connection):
        
        # Log Registration
        Logger().info(f"DB Connection: {connection.name} - Oracle: Initialized")
        
        # Store Database Connection Values
        self.name = connection.name
        self.tns = connection.tns
        self.username = connection.username
        self.password = connection.password
        self.encoding = connection.encoding
        self.nencoding = connection.nencoding
        self._connection = None
    
    # Database connection.
    def connect(self):
        
        # Check if a connection to the database already exists
        if self._instance is None:
            
            try:
                # Attempt to connect to the database
                self._instance = cx_Oracle.connect(
                    user=self.username,
                    password=self.password,
                    dsn=self.tns,
                    encoding=self.encoding,
                    nencoding=self.nencoding
                )
                
                # Log Registration
                Logger().info(f"DB Connection: {self.name} - Oracle: Successful")
                        
            except Exception as e:
                
                # Log Registration
                Logger().info(f"DB Connection: {self.name} - Oracle: Failed, {e}")
                
                raise (f"Database Connection Error {self.name}")
            
        return self._instance

    # Close Database Connection.
    def close(self):
        if self._instance:
            
            # Log Registration
            Logger().info(f"DB Connection: {self.name} - Oracle: Closed")
            
            # Close Connection
            self._instance.close()

    # Query execution with data retrieval. (SELECT)
    def query(self, statement):
        
        # Log Registration
        Logger().info(f"DB Connection: {self.name} - Oracle: Query Execution <{statement}>")
                
        try:
            connection = self.connect()
            cursor = connection.cursor()
            cursor.execute(statement)
            
            # Get query headers
            headers = [desc[0] for desc in cursor.description]

            # Get data rows
            rows = cursor.fetchall()
            
            # Log Registration
            Logger().info(f"DB Connection: {self.name} - Oracle: Query Execution Successful")
            
            # Return a dictionary with headers and rows
            return {
                "headers": headers,
                "rows": rows
            }
        
        except Exception as e:
            
            # Log Registration
            Logger().error(f"DB Connection: {self.name} - Oracle: Query Execution Failed, {e}")
            
            return False
        
    # Insert Query Execution (INSERT).
    def insert(self, statement):
        
        # Log Registration
        Logger().info(f"DB Connection: {self.name} - Oracle: Insert Execution <{statement}>")
                
        try:
            connection = self.connect()
            cursor = connection.cursor()
            cursor.execute(statement)
            connection.commit()
            
            # Log Insert
            Logger().info(f"DB Connection: {self.name} - Oracle: Insert Execution Successful")
            
            return cursor.lastrowid
        except Exception as e:
            
            # Log Registration
            Logger().error(f"DB Connection: {self.name} - Oracle: Insert Execution Failed, {e}")
            
            return False

    # Update Query Execution (UPDATE).
    def update(self, statement):
        
        # Log Registration
        Logger().info(f"DB Connection: {self.name} - Oracle: Update Execution <{statement}>")
                
        try:
            connection = self.connect()
            cursor = connection.cursor()
            cursor.execute(statement)
            connection.commit()
            # Log Insert
            Logger().info(f"DB Connection: {self.name} - Oracle: Update Execution Successful")
            
            return True
        except Exception as e:
            
            # Log Registration
            Logger().error(f"DB Connection: {self.name} - Oracle: Update Execution Failed, {e}")
            
            return False

    # Delete Query Execution (DELETE).
    def delete(self, statement):
        
        # Log Registration
        Logger().info(f"DB Connection: {self.name} - Oracle: Delete Execution <{statement}>")
        
        try:
            connection = self.connect()
            cursor = connection.cursor()
            cursor.execute(statement)
            connection.commit()
            
            # Log Insert
            Logger().info(f"DB Connection: {self.name} - Oracle: Delete Execution Successful")
            
            return True
        except Exception as e:
            
            # Log Registration
            Logger().error(f"DB Connection: {self.name} - Oracle: Delete Execution Failed, {e}")
            
            return False

    # Execute Query (EXEC).
    def exec(self, statement):
        return self.query(statement)
