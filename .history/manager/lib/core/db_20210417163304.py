import sqlite3
import os
from manager.lib.core.log import logger

Class Db(sqlite3):
    def __init__(self,db_path):
        self.db_path = os.path.basename(db_path)
        self.db_name = 
        self.con = self.connect(self.db_path)
        self.cur = self.con.cursor()
        try:
            self.cur.execute("create table services (type, domain, ip, port)")
            logger.info("create database {}".format(self.db_name))
        except sqlite3.OperationalError:
            logger.info("database {} already exists".format(self.db_name))   

    def insert():
        

if __name__ == "__main__":
