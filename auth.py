def register(conn):
    cur = conn.cursor()

    print("Profile registration page")
    print("Please enter the following details")
    username = input("username > ")
    cur.execute("SELECT * FROM users WHERE username='"+username+"'")
    if cur.fetchone():
        print("ERROR: This username already exists. Please try another username.")
        register(conn)
        return
    passwd = input("password > ")
    name = input("name > ")
    phone = int(input("phone > "))
    billing_address = input("billing address > ")
    shipping_address = input("shipping address > ")
    acc_type = "customer"

    if(username == "owner"):
        acc_type = "owner"
    elif(username == "admin"):
        acc_type = "admin"

    cur.execute("INSERT INTO carts VALUES (NULL)")
    cart_id = cur.lastrowid
    cur.execute("INSERT INTO users VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?)", (username, passwd, name, phone, billing_address, shipping_address, acc_type, cart_id))
    conn.commit()

def login(conn):
    cur = conn.cursor()

    print("Login page")
    username = input("username > ")
    cur.execute("SELECT * FROM users WHERE username='"+username+"'")
    if not cur.fetchone():
        print("ERROR: This username does not exist. You must first register.")
        print("Returning to the previous menu...")
        return 

    passwd = input("password > ")

    sql_query = 'SELECT * FROM users WHERE username="' + username + '"'
    cur.execute(sql_query)
    user_row = cur.fetchall()[0]
    user_obj = {"user_id": user_row[0], "username": user_row[1], "name": user_row[3], "phone": user_row[4], "billing_address": user_row[5], "shipping_address": user_row[6], "acc_type": user_row[7],  "cart_id": user_row[8]}

    if(user_row[2] == passwd):
        print("Sucessfully loggned in!")
        return user_obj
    else:
        print("ERROR: Something went wrong with signing you in. Please try again.")
        return None