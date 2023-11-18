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
    query = """SELECT cities.name FROM cities WHERE cities.state_id 
        = (SELECT states.id FROM states WHERE states.name 
        LIKE BINARY %s) """
    cur.execute(query, (sys.argv[4],))
    result = cur.fetchall()
    row= list(rows[0] for rows in result)
    print(", ".join(row))
    conn.close()
