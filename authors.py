def add_author(conn):
    cur = conn.cursor()
    print("")
    print("Author add screen")
    print("Please enter the following details")
    author = input("author name > ")
    cur.execute("INSERT INTO authors VALUES (NULL, '"+author+"')")
    conn.commit()

def menu(conn):
    option = ""

    while option != "return":
        print("")
        print("Please select from one of the following options:")
        print("view authors")
        print("add author")
        print("remove author")
        print("return")

        option = input("> ")

        if(option == "view authors"):
            view_authors(conn)
        elif(option == "add author"):
            add_author(conn)
        elif(option == "remove author"):
            remove_author(conn)

def view_authors(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM authors")
    rows = cur.fetchall()
    
    for row in rows:
        print("=================================================")
        print("author id:", row[0])
        print("author:", row[1])

def getAuthorByID(conn, author_id):
    cur = conn.cursor()
    cur.execute("SELECT name FROM authors WHERE author_id="+str(author_id))
    return cur.fetchone()[0]