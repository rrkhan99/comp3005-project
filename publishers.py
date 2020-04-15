def add_pub(conn):
    cur = conn.cursor()
    print("")
    print("Publisher add screen")
    print("Please enter the following details")

    name = input("name > ")
    email = input("email > ")
    address = input("address > ")
    phone = int(input("phone > "))
    bank_acc = int(input("bank account > "))

    cur.execute("INSERT INTO publishers VALUES (NULL, ?, ?, ?, ?, ?, 0)", (name, email, address, phone, bank_acc))
    conn.commit()

def menu(conn):
    option = ""

    while option != "return":
        print("")
        print("Please select from one of the following options:")
        print("view publishers")
        print("add publisher")
        print("remove publisher")
        print("return")

        option = input("> ")

        if(option == "view publishers"):
            view_publishers(conn)
        elif(option == "add publisher"):
            add_pub(conn)
        elif(option == "remove publisher"):
            remove_pub(conn)

def view_publishers(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM publishers")
    rows = cur.fetchall()
    
    for row in rows:
        print("=================================================")
        print("publisher id:", row[0])
        print("publisher name:", row[1])
        print("publisher email:", row[2])
        print("publisher address:", row[3])
        print("publisher phone:", row[4])
        print("publisher bank account:", row[5])
        print("publisher total earnings:", row[6])

def getPublisherNmaeByID(conn, pub_id):
    cur = conn.cursor()
    cur.execute("SELECT name FROM publishers WHERE pub_id="+str(pub_id))
    return cur.fetchone()[0]