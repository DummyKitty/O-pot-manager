import sqlite3
import os
from manager.lib.core.log import logger
from manager.thirdparty.prettytable import prettytable


class knowledgeDataBase():
    def __init__(self, db_path):
        self.db_path = db_path
        # self.table_name = os.path.basename(db_path).split(".")[0]
        con = sqlite3.connect(self.db_path)
        cur = con.cursor()
        self.white_tables = ["services", "cves", "current_services"]
        try:
            cur.execute(
                """create table services (id INTEGER PRIMARY KEY,type, domain, ip, port)"""
            )
            # cur.execute("create table cves (type, domain, ip, port)")
            cur.execute(
                "create table current_services (id INTEGER PRIMARY KEY,type, domain, ip, port)"
            )
            logger.info("create table services")
            logger.info("create table current_services")

        except sqlite3.OperationalError as ex:
            print(ex)
            # logger.info("table {} already exists".format(self.table_name))
        con.commit()
        con.close()

    def insert(self, table_name, values):
        con = sqlite3.connect(self.db_path)
        cur = con.cursor()
        if table_name in self.white_tables:
            try:
                cur.execute(
                    "insert into {} values (NULL,?,?,?,?)".format(table_name),
                    (values[0], values[1], values[2], values[3]))
            except sqlite3.OperationalError as ex:
                logger.error("sqlite3 insert error")
                print(ex)
        con.commit()
        con.close()

    def delete(self,
               table_name,
               service_type=None,
               domain=None,
               ip=None,
               allrange=None):
        con = sqlite3.connect(self.db_path)
        cur = con.cursor()
        if table_name in self.white_tables:
            try:
                if not allrange:
                    if ip:
                        cur.execute(
                            "delete from {} where ip= ? ".format(table_name),
                            (ip))
                    elif domain:
                        cur.execute(
                            "delete from {} where domain= ? ".format(
                                table_name), (domain))
                    elif service_type:
                        cur.execute("delete from {} where type='{}'".format(
                            table_name, service_type))
                else:
                    cur.execute("delete from services")
            except sqlite3.OperationalError as ex:
                logger.error("sqlite3 delete error")
                print(ex)
        con.commit()
        con.close()

    def select(self,
               table_name,
               service_name=None,
               ip=None,
               port=None,
               limit=None):
        con = sqlite3.connect(self.db_path)
        cur = con.cursor()
        if table_name in self.white_tables:
            try:
                if service_name:
                    cur.execute(
                        "select * from {} where type like '%{}%' ".format(
                            table_name, service_name))
                    result = cur.fetchall()

                else:
                    cur.execute("select * from {} ".format(table_name))
                    result = cur.fetchall()
                con.commit()
                con.close()
                return result
            except sqlite3.OperationalError as ex:
                logger.error("sqlite3 select error")
                print(ex)
        con.commit()
        con.close()

    def update(self, table_name, *values, **kwargs):
        pass


if __name__ == "__main__":
    db = knowledgeDataBase("manager/data/data.db")
    # db.insert("services", ["joomla", "123kn.com", "182.55.223.1", "80"])
    db.delete("services", service_type="wordpress")
    res = db.select("services")
    # print(res)
    tb = prettytable.PrettyTable(
        ["id", "service_type", "domain", "ip", "port"])
    for i in res:
        tb.add_row(list(i))
    print(tb)