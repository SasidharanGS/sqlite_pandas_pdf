import sqlite3

with sqlite3.connect('sales.db') as conn:
    # Get the cursor
    cursor = conn.cursor()

    # Execute a query to retrieve the table names
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

    # Fetch all the table names
    tables = cursor.fetchall()

    for t in tables:
            table_name = t[0]
            print(f"\nTable: {table_name}")

            # Execute a query to retrieve all rows from the table
            cursor.execute(f"SELECT * FROM {table_name};")

            # Fetch all rows
            rows = cursor.fetchall()

            # Print column names
            column_names = [description[0] for description in cursor.description]
            print(", ".join(column_names))

            # Print data
            for row in rows:
                print(", ".join(str(value) for value in row))
