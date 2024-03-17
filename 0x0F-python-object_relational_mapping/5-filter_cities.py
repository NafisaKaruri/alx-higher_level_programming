#!/usr/bin/python3
"""List all cities from the database hbtn_0e_4_usa"""


from sys import argv
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost",
                           port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3],
                           charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM cities \
                INNER JOIN states on cities.state_id = states.id \
                WHERE states.name LIKE BINARY '{}'".format(argv[4]))
    cities = cur.fetchall()
    print(", ".join(city[2] for city in cities))
    cur.close()
    conn.close()
