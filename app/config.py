import os

class Config(object):
    DEBUG = True
    CSRF_ENABLED = True

class Configdb(Config):
    PARAMETER = ("DRIVER={SQL Server};"
                                 "SERVER=EDGOCH-27062019\SQL2016;"
                                 "DATABASE=VIC_Connector_DEV;"
                                 # "UID=user;"
                                 # "PWD=password"
                                 "Trusted_Connection=yes" # User for Windows authentication
                                 )
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') # "mssql+pyodbc:///?odbc_connect="