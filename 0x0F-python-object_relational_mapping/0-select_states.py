#!/usr/bin/python3
"""
    Select States module
"""


def connect(username, passwd, dbname):
    """Creates a database connection
    """
    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=passwd,
        db=dbname
    )
    return conn


if __name__ == "__main__":
    import MySQLdb
    import sys

    """Select states table from a database
    """
    conn = connect(sys.argv[1], sys.argv[2], sys.argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    result = cur.fetchall()
    for row in result:
        print(row)
    conn.close()
