import connection
import auth
import users
import publishers
import genres
import books
import authors

def main():
    conn = connection.connect()
    print("Welcome to Look Inna Bookstore")
    print("Note: In order to be able to checkout, you will first need to register.")

    login_obj = None
    option = ""
    while option != "exit":
        print("")
        if(login_obj):
            print("You are currently signed in as", login_obj["username"])
        print("Please select from one of the following options:")
        print("shop")
        print("view checkout cart")
        if(login_obj):
            print("checkout")
            print("order lookup")
            print("logout")
            if(login_obj["acc_type"] == "owner" or login_obj["acc_type"] == "admin"):
                print("manage publishers")
                print("manage authors")
                print("manage books")
                print("manage genres")
                if(login_obj["acc_type"] == "owner"):
                    print("manage users")
                    print("view report")
        else:
            print("login")
            print("register")
        print("exit")

        option = input("> ")

        if (option == "login"):
            login_obj = auth.login(conn)
        elif (option == "register"):
            auth.register(conn)
        elif(option == "logout"):
            login_obj = None
        elif(login_obj):
            if(option == "manage publishers" and (login_obj["acc_type"] == "owner" or login_obj["acc_type"] == "admin")):
                publishers.menu(conn)
            elif(option == "manage genres" and (login_obj["acc_type"] == "owner" or login_obj["acc_type"] == "admin")):
                genres.menu(conn)
            elif(option == "manage books" and (login_obj["acc_type"] == "owner" or login_obj["acc_type"] == "admin")):
                books.menu(conn)
            elif(option == "manage authors" and (login_obj["acc_type"] == "owner" or login_obj["acc_type"] == "admin")):
                authors.menu(conn)
            elif(option == "manage users" and login_obj["acc_type"] == "owner"):
                users.menu(conn)

    conn.close()

main()