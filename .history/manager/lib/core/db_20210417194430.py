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
        if table_name in self.white_tables:
            try:
                self.cur.execute("insert into {} values (?, ?, ?, ?)".format(table_name),(values))
            except sqlite3.OperationalError as ex:
                logger.error("sqlite3 operation error")
                print(ex)
    def delete(self,table_name,domain=None, IP=None):
        if table_name in self.white_tables: 
            try:
                if IP :
                    self.cur.execute("delete from {} where domane=? )".format(table_name),(domain))
                elif domain:
                    self.cur.execute("delete from {} where domane=? )".format(table_name),(domain))
            except sqlite3.OperationalError as ex:
                logger.error("sqlite3 operation error")
                print(ex)

    def select(self,table_name,*values,**kwargs):

    def update(self,table_name,*values,**kwargs):


if __name__ == "__main__":
