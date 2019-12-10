import logging
import pyodbc

# Singleton desing for the DB Connection
# The inner class is created once so everytime the singleton class is instantiated then it will return the first initally instantiated class
# This helps to keep the same pool of connections for a DB and relegating the load balancing and pool managment to the DB

class db:
    class __db:
        def __init__(self):
            try:
                self.connection = pyodbc.connect('Driver={SQL Server};'
                                    'Server=EDGOCH-27062019\SQL2016;'
                                    'Database=VIC_Connector_DEV;'
                                    'Trusted_Connection=yes;')
                self.cursor = self.connection.cursor()
                logging.DEBUG('DB Singleton Object created')
            except:
                logging.ERROR('Unable to connect to DB')
                raise Exception('Not able to adquire db connection')
            
        
        def query(self,query,params=[]):
            try:
                if params: 
                    return self.cursor.execute(query,params)
                else:
                    return self.cursor.execute(query)
            except:
                logging.ERROR('Unable to connect to perform the following query: \n {}'.format(query))
                raise Exception('Not able to perform query. Error: \n {}'.format(query))
                return None

        def __del__(self):
            self.connection.close()

        def __str__(self):
            return repr(self) + self.val

    instance = None

    def __init__(self, arg = ''):
        if not db.instance:
            db.instance = db.__db()
            logging.DEBUG('Reusing Singleton DB Object')
        else:
            db.instance.val = arg
    def __getattr__(self, name):
        return getattr(self.instance, name)