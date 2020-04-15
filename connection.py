import sqlite3

def connect():
    conn = sqlite3.connect("bookstore.db")
    cur = conn.cursor()
    cur.execute("PRAGMA foreign_keys = ON")
    cur.execute("CREATE TABLE IF NOT EXISTS carts(cart_id INTEGER PRIMARY KEY)")
    cur.execute("CREATE TABLE IF NOT EXISTS users(user_id INTEGER PRIMARY KEY, username TEXT UNIQUE, passwd TEXT, name TEXT, phone INTEGER, billing_address TEXT, shipping_address TEXT, acc_type TEXT, cart_id INTEGER, FOREIGN KEY (cart_id) REFERENCES carts(cart_id) ON DELETE CASCADE)")
    cur.execute("CREATE TABLE IF NOT EXISTS publishers(pub_id INTEGER PRIMARY KEY, name TEXT, email TEXT, address TEXT, phone INTEGER, bank_acc INTEGER, earnings REAL DEFAULT 0)")
    cur.execute("CREATE TABLE IF NOT EXISTS genres(genre_id INTEGER PRIMARY KEY, genre TEXT UNIQUE)")
    cur.execute("CREATE TABLE IF NOT EXISTS books(isbn INTEGER PRIMARY KEY, title TEXT, pub_id INTEGER, genre_id INTEGER, price REAL, num_pages INTEGER, stock INTEGER, percentage REAL, FOREIGN KEY (pub_id) REFERENCES publishers(pub_id), FOREIGN KEY (genre_id) REFERENCES genres(genre_id) ON DELETE CASCADE)")
    cur.execute("CREATE TABLE IF NOT EXISTS authors(author_id INTEGER PRIMARY KEY, name TEXT)")
    conn.commit()
    return conn

def close(conn):
    conn.close()