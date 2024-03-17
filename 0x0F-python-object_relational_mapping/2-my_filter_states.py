#!/usr/bin/python3
"""List all states with a name matching argument from the database"""


from sys import argv
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost",
                           port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3],
                           charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'".format(argv[4]))
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    conn.close()
