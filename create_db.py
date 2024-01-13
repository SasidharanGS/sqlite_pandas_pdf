import sqlite3
import random
import datetime

#CREATE TABLES SALES, CUSTOMERS, PRODUCTS:
create_sales_table = '''
    CREATE TABLE sales(
        sale_id INTEGER PRIMARY KEY,
        sale_date DATE,
        customer_id INTEGER,
        product_id INTEGER,
        quantity INTEGER,
        unit_price DECIMAL(10,2),
        total_price DECIMAL(10,2),
        FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
        FOREIGN KEY (product_id) REFERENCES products(product_id)
    )
'''
create_customers_table = '''
    CREATE TABLE customers(
        customer_id INTEGER PRIMARY KEY,
        f_name TEXT,
        l_name TEXT,
        email TEXT,
        phone TEXT
    )
'''
create_products_table = '''
    CREATE TABLE products(
        product_id INTEGER PRIMARY KEY,
        name TEXT,
        unit_cost DECIMAL(10,2)
    )
'''

#INSERT DATA INTO TABLES:
insert_sales = '''
    INSERT INTO sales (sale_date, customer_id, product_id, quantity, unit_price, total_price) VALUES (?,?,?,?,?,?)
'''
insert_customers = '''
    INSERT INTO customers (f_name, l_name, email, phone) VALUES(?,?,?,?)
'''
insert_products = '''
    INSERT INTO products (name, unit_cost) VALUES(?,?)
'''

#SAMPLE DATA:
products = [('Product A', 50.00), ('Product B', 25.00), ('Product C', 75.00), ('Product D', 40.00), ('Product E', 60.00)]

customers = [
    ('John', 'Doe', 'johndoe@example.com', '555-1234'),
    ('Jane', 'Doe', 'janedoe@example.com', '555-5678'),
    ('Bob', 'Smith', 'bobsmith@example.com', '555-9012'),
    ('Alice', 'Jones', 'alicejones@example.com', '555-3456'),
    ('David', 'Brown', 'davidbrown@example.com', '555-7890'),
    ('Emily', 'Davis', 'emilydavis@example.com', '555-2345'),
    ('Frank', 'Wilson', 'frankwilson@example.com', '555-6789'),
    ('Grace', 'Lee', 'gracelee@example.com', '555-1234'),
    ('Henry', 'Chen', 'henrychen@example.com', '555-5678'),
    ('Isabel', 'Garcia', 'isabelgarcia@example.com', '555-9012')
]

# Define the start and end dates for generating sales data
start_date = datetime.date(2022, 1, 1)
end_date = datetime.date(2022, 12, 31)

# Connect to the database and create the tables
with sqlite3.connect('sales.db') as conn:
    
    conn.execute(create_sales_table)
    conn.execute(create_products_table)
    conn.execute(create_customers_table)

    for product in products:
        conn.execute(insert_products, product)

    for customer in customers:
                conn.execute(insert_customers, customer)

    # Insert sample data into the sales table
    for i in range(1000):
        sale_date = start_date + datetime.timedelta(days=random.randint(0, 364))
        customer_id = random.randint(1, len(customers))
        product_id = random.randint(1, len(products))
        quantity = random.randint(1, 10)
        unit_price = products[product_id-1][1]
        total_price = quantity * unit_price
        conn.execute(insert_sales, (sale_date, customer_id, product_id, quantity, unit_price, total_price))

    # Commit the changes
    conn.commit()

    print("Database successfully created!")
