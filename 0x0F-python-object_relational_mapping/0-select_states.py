#!/usr/bin/python3
"""List all states rom the database hbtn_0e_0_usa"""


from sys import argv
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost",
                           port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3],
                           charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states")
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    conn.close()
