import sqlite3
import os
from manager.lib.core.log import logger

Class Db(sqlite3):
    def __init__(self,db_path):
        self.db_path = os.sys.db_path
        self.db_name = 
        self.con = self.connect(self.db_path)
        self.cur = self.con.cursor()
        try:
            self.cur.execute("create table services (type, domain, ip, port)")
            logger.info("create database {}".format(self.data_path))
        except sqlite3.OperationalError:
            
            

if __name__ == "__main__":
