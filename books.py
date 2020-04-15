import publishers
import genres

def menu(conn):
    option = ""

    while option != "return":
        print("")
        print("Please select from one of the following options:")
        print("view books")
        print("add book")
        print("remove book")
        print("return")

        option = input("> ")

        if(option == "view books"):
            view_books(conn)
        elif(option == "add book"):
            add_book(conn)
        elif(option == "remove book"):
            remove_book(conn)

def add_book(conn):
    cur = conn.cursor()
    print("")
    print("Book add screen")
    print("Please enter the following details")

    isbn = int(input("ISBN > "))
    cur.execute("SELECT * FROM books WHERE isbn="+str(isbn))
    if cur.fetchone():
        print("ERROR: A book already exists with this ISBN. Please try again with a different ISBN.")
        add_book(conn)

    title = input("title > ")
    num_authors = int(input("number of authors > "))
    authors = []
    for x in range(num_authors):
        author = input("author " + str(x + 1) + " > ")
        authors.append(author)
    pub = input("publisher > ")
    cur.execute("SELECT * FROM publishers WHERE name='"+pub+"'")
    if not cur.fetchone():
        print("ERROR: This publisher does not exist. You must first create this publisher")
        print("Redirecting you to the add publisher screen...")
        publishers.add_pub(conn)
        add_book(conn)
    
    cur.execute("SELECT pub_id FROM publishers WHERE name='"+pub+"'")
    pub_id = cur.fetchone()[0]

    genre = input("genre > ")
    cur.execute("SELECT * FROM genres WHERE genre='"+genre+"'")
    if not cur.fetchone():
        print("ERROR: This genre does not exist. You must first create this genre")
        print("Redirecting you to the add genre screen...")
        genres.add_genre(conn)
        add_book(conn)
    
    cur.execute("SELECT genre_id FROM genres WHERE genre='"+genre+"'")
    genre_id = cur.fetchone()[0]

    price = float(input("price > "))
    num_pages = int(input("number of pages > "))
    stock = int(input("stock > "))
    percentage = float(input("publisher's share percentage > "))

    cur.execute("INSERT INTO books VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (isbn, title, pub_id, genre_id, price, num_pages, stock, percentage))
    conn.commit()

def view_books(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM books")
    rows = cur.fetchall()
    
    for row in rows:
        print("=================================================")
        print("book isbn:", row[0])
        print("book title:", row[1])
        print("publisher name:", publishers.getPublisherNmaeByID(conn, row[2]))
        print("genre: ", genres.getGenreByID(conn, row[3]))
        print("price:", row[4])
        print("number of pages:", row[5])
        print("stock:", row[6])
        print("publisher's share percentage:", row[7])