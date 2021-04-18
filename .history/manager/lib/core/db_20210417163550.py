import sqlite3
import os
from manager.lib.core.log import logger

Class Db(sqlite3):
    def __init__(self,db_path):
        self.db_path = os.path.basename(db_path)
        self.db_name = 
        self.con = self.connect(self.db_path)
        self.cur = self.con.cursor()
        self.white_tables = ["services","cves"]
        try:
            self.cur.execute("create table services (type, domain, ip, port)")
            logger.info("create database {}".format(self.db_name))
        except sqlite3.OperationalError:
            logger.info("database {} already exists".format(self.db_name))   

    def insert(self,table_name,*values,**kwargs):
        
        if table_name not in self.white_tables:
            self.cur.execute("insert into {} values (?, ?, ?, ?)".table_name,
                ("wordpress", "123kn.com", "133.5.1.22", "80"))


if __name__ == "__main__":
