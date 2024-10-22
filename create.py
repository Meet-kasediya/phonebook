import sqlite3 #interact with SQLite databases
myconn = sqlite3.connect('database1.db') # opens a connection to a SQLite database file




# CREATE TABLE IF NOT EXISTS contacts (
#     contact_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     contact_firstname TEXT,
#     contact_lastname TEXT,
#     contact_email TEXT,
#     contact_no TEXT,
#     contact_address TEXT,
#     contact_organisation TEXT

# CREATE TABLE IF NOT EXISTS category (
#     category_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     category_name TEXT

# CREATE TABLE IF NOT EXISTS contact_category (
#     cc_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     contact_id INTEGER,
#     category_id INTEGER,
#     FOREIGN KEY (contact_id) REFERENCES contact(contact_id),
#     FOREIGN KEY (category_id) REFERENCES category(category_id)
# );