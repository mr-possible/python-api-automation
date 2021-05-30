import os
import mysql.connector
from mysql.connector import Error
import logging
from utils.configurations import getConfig

logging.basicConfig(filename=os.pardir + os.sep + 'logs' + os.sep + 'dblogs.log',
                    filemode='w',
                    format='%(asctime)s %(message)s', datefmt='[[%m/%d/%Y %I:%M:%S %p]]',
                    level=logging.DEBUG
                    )


class DbUtil:
    __dbhost = ''
    __dbName = ''
    __dbusername = ''
    __dbpassword = ''
    __conn = None

    def __init__(self):
        config = getConfig()
        self.__dbhost = config['SQL']['host']
        self.__dbName = config['SQL']['database']
        self.__dbusername = config['SQL']['user']
        self.__dbpassword = config['SQL']['password']

    def giveMeConnection(self):
        try:
            self.__conn = mysql.connector.connect(user=self.__dbusername,
                                                  password=self.__dbpassword,
                                                  host=self.__dbhost,
                                                  database=self.__dbName)
            if self.__conn.is_connected():
                logging.info(
                    f'DB Connection established on port :: {self.__conn.server_port} and using database :: {self.__dbName}')
            return self.__conn
        except Error as err:
            logging.info(
                f'DB Connection encountered error :: {err}')

    def fetchOneRecord(self, query):
        """
        @param query: SQL Query to get data from the database as per needs.
        @return: Returns a tuple of record obtained by querying the database using @param : query
        """
        self.__conn = self.giveMeConnection()
        cursor = self.__conn.cursor()
        assert self.__conn, 'Connection is not established !! Check for any error or malicious code.'
        cursor.execute(query)
        return cursor.fetchone()

    def __del__(self):
        if self.__conn:
            self.__conn.close
