def menu(conn):
    option = ""

    while option != "return":
        print("")
        print("Please select from one of the following options:")
        print("view users")
        print("add admin")
        print("remove user")
        print("return")

        option = input("> ")

        if(option == "view users"):
            view_users(conn)
        elif(option == "add admin"):
            add_admin(conn)
        elif(option == "remove user"):
            remove_user(conn)

def view_users(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()
    
    for row in rows:
        print("=================================================")
        print("user id:", row[0])
        print("username:", row[1])
        print("password:", row[2])
        print("name:", row[3])
        print("phone:", row[4])
        print("billing address:", row[5])
        print("shipping address:", row[6])
        print("account type:", row[7])
        print("cart id:", row[8])

def add_admin(conn):
    cur = conn.cursor()

    print("Admin registration page")
    print("Please enter the following details")
    username = input("username > ")
    passwd = input("password > ")
    name = input("name > ")
    phone = int(input("phone > "))
    billing_address = input("billing address > ")
    shipping_address = input("shipping address > ")
    acc_type = "admin"

    cur.execute("INSERT INTO carts VALUES (NULL)")
    cart_id = cur.lastrowid
    cur.execute("INSERT INTO users VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?)", (username, passwd, name, phone, billing_address, shipping_address, acc_type, cart_id))
    conn.commit()