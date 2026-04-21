import mysql.connector
from mysql.connector import errorcode

class Database:
    def __init__(self, user='root', password='HoangQu@n123',
                              host='127.0.0.1',
                              database='LoVuongWallet'):
        self.user = user
        self.password = password
        self.host = host
        self.database = database
    
    def ConnectDatabase(self):
            database = Database()
            try:
                cnx = mysql.connector.MySQLConnection(self.user, self.password/
                                                self.host, self.database)
            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                    print("Something is wrong with your user name or password")
                elif err.errno == errorcode.ER_BAD_DB_ERROR:
                    print("Database does not exist")
                else:
                    print(err)
            else:
                cnx.close()

    def InsertTable(self, cmd):
        self.ConnectDatabase()
        try:
            pass
        except:
            pass

    def UpdateTable(self, cmd):
        self.ConnectDatabase()
        try:
            pass
        except:
            pass

    def DeleteTable(self, cmd):
        self.ConnectDatabase()
        try:
            pass
        except:
            pass
        