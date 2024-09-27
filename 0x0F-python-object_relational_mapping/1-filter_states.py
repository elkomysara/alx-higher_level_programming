#!/usr/bin/python3
"""
Module that lists all states starting with 'N' from the database
"""

if __name__ == "__main__":

    import MySQLdb
    from sys import argv

    # Connect to database using command-line arguments
    my_database = MySQLdb.connect(
        host='localhost',
        user=argv[1],
        password=argv[2],
        db=argv[3],
        port=3306
    )

    # define cursor used to execute mysql queries
    my_cursor = my_database.cursor()

    # Execute a SELECT query to find states starting with 'N'
    my_cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC;")

    # fetch all the data returned by the query
    my_data = my_cursor.fetchall()

    # Iterate through the fetched data and print each row
    for row in my_data:
        print(row)

    # Close all cursors
    my_cursor.close()

    # Close all databases
    my_database.close()
