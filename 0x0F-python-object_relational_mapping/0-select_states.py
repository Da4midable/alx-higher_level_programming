#!/usr/bin/python3
"""This script lists all states from hbtn_0e_0_usa database"""

import MySQLdb
import sys


if __name__ == "__main__":
    base = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    iterator = base.cursor()
    iterator.execute("SELECT * FROM states")
    rows = iterator.fetchall()
    for row in rows:
        print(row)
    iterator.close()
    base.close()
