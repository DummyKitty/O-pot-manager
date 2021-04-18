import sqlite3
import os
from manager.lib.core.log import logger


class knowledgeDataBase():
    def __init__(self, db_path):
        self.db_path = db_path
        self.table_name = os.path.basename(db_path).split(".")[0]
        self.con = sqlite3.connect(self.db_path)
        self.cur = self.con.cursor()
        self.white_tables = ["services", "cves"]
        try:
            self.cur.execute("create table {} (type, domain, ip, port)".format(
                self.table_name))
            logger.info("create table {}".format(self.table_name))
        except sqlite3.OperationalError as ex:
            print(ex)
            logger.info("table {} already exists".format(self.table_name))
        self.con.commit()

    def insert(self, table_name, values):
        if table_name in self.white_tables:
            try:
                self.cur.execute(
                    "insert into {} values (?,?,?,?)".format(table_name),
                    (values[0], values[1], values[2], values[3]))
            except sqlite3.OperationalError as ex:
                logger.error("sqlite3 operation error")
                print(ex)
        self.con.commit()

    def delete(self, table_name, domain=None, ip=None):
        if table_name in self.white_tables:
            try:
                if ip:
                    self.cur.execute(
                        "delete from {} where ip=? )".format(table_name), (ip))
                elif domain:
                    self.cur.execute(
                        "delete from {} where domane=? )".format(table_name),
                        (domain))
            except sqlite3.OperationalError as ex:
                logger.error("sqlite3 operation error")
                print(ex)
        self.con.commit()

    def select(self, table_name, service_name):
        if table_name in self.white_tables:
            try:
                if service_name:
                    self.cur.execute(
                        "select * from {} where type like ?".format(
                            table_name), (service_name))
                    return self.cur.fetchall()
            except sqlite3.OperationalError as ex:
                logger.error("sqlite3 operation error")
                print(ex)
        self.con.commit()

    def update(self, table_name, *values, **kwargs):
        pass


if __name__ == "__main__":
    db = knowledgeDataBase("manager/data/servicedb/services.db")
    db.insert("services", ["wordpress", "123kn.com", "182.55.223.1", "80"])
    print(db.select("services", "wordpress"))
