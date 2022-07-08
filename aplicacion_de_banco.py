list_users = list ()

class user:
    name = ""
    last_name = ""
    id = 0
    account_balance = 0


def show_menssage(menssage):
 print(menssage)

def register_user():
    person = user()
    person.name = input("Enter your name: ")
    person.last_name = input("Enter your last name: ")
    person.id = input("Enter your ID: ")
    person.account_balance = int(input("Enter your account balance: "))

    list_users.append(person)
    show_menssage(" ---------Registered user---------")

def list_users_and_balance():
    
    for person in list_users:
        print(person.name ,  person.last_name , person.id , person.account_balance)

def delete_user():
    eliminated_user = input("Enter the id of the person to remove: " )
    i = 0
    for user in list_users:
        if user.id == eliminated_user:
            list_users.pop(i)
            show_menssage("="*60)
            show_menssage("We have removed this id {}".format(user.id))
            show_menssage("="*60)
        i+=1

    list_users_and_balance()

def editing_information():
    edited_user = input("Enter the id of the person to modify: ")
    x = 0
    for user in list_users:
        if user.id == edited_user:
            list_users[x].name = input("Enter the new name: ")
            list_users[x].last_name = input("Enter the new last name: ")
            list_users[x].id = input("Enter the new id: ")
            list_users[x].account_balance = input("Enter the new account balance: ")
        x+=1
    list_users_and_balance()
    show_menssage("Edited information")
     
def log_out():
    show_menssage("You have logged out")

def menu():
    option = 0
    while option !=5:
        print ("========Menu========")
        print ("1.- Register user")
        print ("2.- List of users and their balance account")
        print ("3.- Delete user")
        print ("4.- Edit user information")
        print ("5.- Logged out")

        while True:
            try:
                option = int(input("Please, write a number: "))
                break
            except ValueError:
                print("Oops!  That was not a number.  Try again...")
        print(option)
       
        if option == 1:
            register_user()
            
        elif option == 2:
            list_users_and_balance()
            
        elif option == 3:
            delete_user()
            
        elif option == 4:
            editing_information()
 
    log_out()

menu()