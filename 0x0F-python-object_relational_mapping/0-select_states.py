#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys


def main():
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=db_name,
            charset="utf8"
        )

    except MySQLdb.Error as e:
        print("MySQLdb Error: {}".format(e))
        sys.exit(1)

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    for state in cursor.fetchall():
        print(state)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
