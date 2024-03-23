import mysql.connector as mysql
import sys
import re
import traceback
import datetime
import os

class Database():
    def log(self,parsename,detail):
        if not os.path.exists(path="log" + "/"):
            os.makedirs(name="log" + "/")

        path = "log  " + "/" + parsename + ".log"

        if os.path.isfile(path) is not True:
            f = open(path, "w+")
            f.close()

        with open(path, "a") as f:
            f.write("hora: " + str(datetime.datetime.now()) + "\n")
            f.write(str(detail) + "\n")
            f.write("\n")

    def __init__(self):
        self.server= "192.168.0.234"
        self.database = ""
        self.username = ""
        self.password = ""

        if self.password is None:
            self.password = ""

        self.conn = mysql.connect(user=self.username, password=self.password, host = self.server, database = self.database)
        self.cursor = self.conn.cursor(dictionary = True)

    def commit(self):
        self.conn.commit()
        