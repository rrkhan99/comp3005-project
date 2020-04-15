def add_genre(conn):
    cur = conn.cursor()
    print("")
    print("Publisher add screen")
    print("Please enter the following details")
    genre = input("genre > ")
    cur.execute("INSERT INTO genres VALUES (NULL, '"+genre+"')")
    conn.commit()

def menu(conn):
    option = ""

    while option != "return":
        print("")
        print("Please select from one of the following options:")
        print("view genres")
        print("add genre")
        print("remove genre")
        print("return")

        option = input("> ")

        if(option == "view genres"):
            view_genres(conn)
        elif(option == "add genre"):
            add_genre(conn)
        elif(option == "remove genre"):
            remove_genre(conn)

def view_genres(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM genres")
    rows = cur.fetchall()
    
    for row in rows:
        print("=================================================")
        print("genre id:", row[0])
        print("genre:", row[1])

def getGenreByID(conn, genre_id):
    cur = conn.cursor()
    cur.execute("SELECT genre FROM genres WHERE genre_id="+str(genre_id))
    return cur.fetchone()[0]