PRAGMA foreign_keys = ON
CREATE TABLE IF NOT EXISTS carts(cart_id INTEGER PRIMARY KEY)
CREATE TABLE IF NOT EXISTS users(user_id INTEGER PRIMARY KEY, username TEXT UNIQUE, passwd TEXT, name TEXT, phone INTEGER, billing_address TEXT, shipping_address TEXT, acc_type TEXT, cart_id INTEGER, FOREIGN KEY (cart_id) REFERENCES carts(cart_id) ON DELETE CASCADE)
CREATE TABLE IF NOT EXISTS publishers(pub_id INTEGER PRIMARY KEY, name TEXT, email TEXT, address TEXT, phone INTEGER, bank_acc INTEGER, earnings REAL DEFAULT 0)
CREATE TABLE IF NOT EXISTS genres(genre_id INTEGER PRIMARY KEY, genre TEXT UNIQUE)
CREATE TABLE IF NOT EXISTS books(isbn INTEGER PRIMARY KEY, title TEXT, pub_id INTEGER, genre_id INTEGER, price REAL, num_pages INTEGER, stock INTEGER, percentage REAL, FOREIGN KEY (pub_id) REFERENCES publishers(pub_id), FOREIGN KEY (genre_id) REFERENCES genres(genre_id) ON DELETE CASCADE)
CREATE TABLE IF NOT EXISTS authors(author_id INTEGER PRIMARY KEY, name TEXT)
INSERT INTO authors VALUES (NULL, ?)
SELECT * FROM authors
SELECT name FROM authors WHERE author_id=?
SELECT * FROM books WHERE isbn=?
SELECT * FROM publishers WHERE name=?
SELECT pub_id FROM publishers WHERE name=?
SELECT * FROM genres WHERE genre=?
SELECT genre_id FROM genres WHERE genre=?
INSERT INTO books VALUES (?, ?, ?, ?, ?, ?, ?, ?)
SELECT * FROM users WHERE username=?
INSERT INTO carts VALUES (NULL)
INSERT INTO users VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?)
INSERT INTO genres VALUES (NULL,?)
SELECT * FROM genres
SELECT genre FROM genres WHERE genre_id=?
INSERT INTO publishers VALUES (NULL, ?, ?, ?, ?, ?, 0)
SELECT name FROM publishers WHERE pub_id=?
INSERT INTO carts VALUES (NULL)
INSERT INTO users VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?)