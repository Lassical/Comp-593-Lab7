"""
Description:
 Creates the people table in the Social Network database
 and populates it with 200 fake people.

Usage:
 python create_db.py
"""
import os
import inspect
from faker import Faker
import sqlite3
from datetime import datetime


def main():
    global db_path
    db_path = os.path.join(get_script_dir(), 'social_network.db')
    create_people_table()
    populate_people_table()

def create_people_table():
    """Creates the people table in the database"""

    # Open a connection to the database.
    con = sqlite3.connect('social_network.db')
    # Get a Cursor object that can be used to run SQL queries on the database.

    cur = con.cursor()
    # Define an SQL query that creates a table named 'people'.

    create_ppl_tbl_query = """
    CREATE TABLE IF NOT EXISTS people
    (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    address TEXT NOT NULL,
    city TEXT NOT NULL,
    province TEXT NOT NULL,
    bio TEXT,
    age INTEGER,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL
    );
    """
    # Execute the SQL query to create the 'people' table.
    cur.execute(create_ppl_tbl_query)
    # Commit (save) pending transactions to the database.

    con.commit()
    # Close the database connection.

    con.close()

    return

def populate_people_table():
    """Populates the people table with 200 fake people"""

    con = sqlite3.connect('social_network.db')
    cur = con.cursor()
    
    add_person_query = """
    INSERT INTO people
    (
    name,
    email,
    address,
    city,
    province,
    bio,
    age,
    created_at,
    updated_at
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
    """

    # Define tuple of data for new person to insert into people table
    # Data values must be in same order as specified in query
    fake = Faker("en_CA")
    for _ in range(200):
        new_person = (fake.name(),
        fake.email(),
        fake.street_address(),
        fake.city(),
        fake.administrative_unit(),
        fake.sentence(nb_words=10),
        fake.random_int(min = 1, max = 99),
        datetime.now(),
        datetime.now())
        # Execute query to add new person to people table
        cur.execute(add_person_query, new_person)
    con.commit()
    con.close()
    return

def get_script_dir():
    """Determines the path of the directory in which this script resides

    Returns:
        str: Full path of the directory in which this script resides
    """
    script_path = os.path.abspath(inspect.getframeinfo(inspect.currentframe()).filename)
    return os.path.dirname(script_path)

if __name__ == '__main__':
   main()