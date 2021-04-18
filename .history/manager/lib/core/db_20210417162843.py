import sqlite3

Class Db(sqlite3):
    def __init__(self,db_path):
        self.db_path = db_path
        self.con = self.connect(self.db_path)
        self.cur = self.con.cursor()
        try:
            self.
            

if __name__ == "__main__":
