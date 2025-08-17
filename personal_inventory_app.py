# personal inventory app

import os
import time
import psycopg2 # import database dependency for postgres /// change this description later

# connect the database
conn = psycopg2.connect(
    database='personal_inventory_DB',
    user='postgres',
    password='inventory123',
    host='localhost',
    port='5432',
)
cursor = conn.cursor() # cursor variable to be used for executing commands to postgres

def main():
    cursor.execute("""
            CREATE TABLE IF NOT EXISTS categories (
            category_id SERIAL PRIMARY KEY,
            category_name TEXT UNIQUE NOT NULL
            );
            """)
    conn.commit()

    # start program with table creation
    cursor.execute("""
                CREATE TABLE IF NOT EXISTS inventory (
                id SERIAL PRIMARY KEY,
                category_id INT NOT NULL,
                item TEXT NOT NULL,
                quantity INT NOT NULL,
                FOREIGN KEY (category_id) REFERENCES categories (category_id)
                );
                """)
    conn.commit() # committing changes to database... need this after every change to the database

    default_categories = [
        'Electronics',
        'Furniture',
        'Tools & Supplies',
        'Perishables',
        'Clothing',
        'Cleaning & Maintenance',
        'Medical',
        'Misc'
    ]

    for category in default_categories:
        cursor.execute("""
                    INSERT INTO categories (category_name) VALUES (%s)
                    ON CONFLICT (category_name) DO NOTHING;
                    """, (category,))
    conn.commit()

        


# CRUD functions
def add_inventory():
    while True:
        new_inventory = input('Please enter the Category, Item, and Quantity as formatted below:\n\n'
                            '[category id], [item], [quantity]: ').lower()
        if new_inventory.strip() == 'x':
            break
        else:
            try:
                category_id, item, quantity = new_inventory.split(',')
            except:
                print('Please complete all fields.\n')
                continue
            try:
                quantity = int(quantity.strip())
                cursor.execute("INSERT INTO inventory (category_id, item, quantity) VALUES (%s, %s, %s);",
                                (category_id.strip(), item.strip(), int(quantity)))
                conn.commit()
            except ValueError:
                print('Please enter a valid integer for quantity.\n\n')
                continue



def read_inventory():
    # read all inventory
    cursor.execute("""
                   SELECT categories.category_name,
                   inventory.item,
                   SUM(inventory.quantity) AS total_quantity
                   FROM inventory
                   JOIN categories ON inventory.category_id = categories.category_id
                   GROUP BY categories.category_name, inventory.item
                   ORDER BY categories.category_name, inventory.item;
                   """)
    allRows = cursor.fetchall()
    for cat_name, inv_item, inv_quantity in allRows:
        print(f'{cat_name}: {inv_item} | Qty: {inv_quantity}')

    cursor.execute("""
                   SELECT * FROM categories;
                   """)
    columns = cursor.fetchall()
    # read categories only
    for id, column in columns:
        print(f'{id}: {column}')



def edit_inventory():
    # edit inventory based on ID


    """
    ***** SQL code for edit func ******

    update inventory
set
	category = 'whatintheworld'
where id = 5;

select * from inventory order by id
    """

    # edit inventory based on ...
    return

def remove_inventory():
    return

main()
add_inventory()
read_inventory()

cursor.close() # close the cursor
conn.close() # close the connection once the program is done
