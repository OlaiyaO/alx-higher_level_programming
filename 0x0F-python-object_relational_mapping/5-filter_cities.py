#!/usr/bin/python3
"""
Script that lists all cities of a given state from the database hbtn_0e_4_usa
"""
import MySQLdb
import sys


def main():
    """
    Main function to connect to MySQL database and list cities by state
    """
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=db_name
        )
    except MySQLdb.Error as e:
        print("MySQLdb Error:", e)
        sys.exit(1)

    cursor = db.cursor()
    query = """
        SELECT cities.id, cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """
    cursor.execute(query, (state_name,))

    cities = cursor.fetchall()

    if cities:
        print(", ".join([city[1] for city in cities]))

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
