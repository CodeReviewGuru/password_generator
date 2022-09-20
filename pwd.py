import generator
import storage

try:
    init_input = input("Is this for uname ('user') or password ('pass')? Type 'q' to exit program:  ")
    while init_input != 'q':
        if init_input == 'user':
            usr_input = input("Type 'gen' to Generate, 'ret' to Retrieve username? ")
            if usr_input == 'gen':
                answer = "yes"
                while answer == "yes":
                    username = generator.user_gen()
                    print("Your username is: " + username)
                    store = input("Would you like to save username 'y/n':  ")
                    if store == 'y':
                      storage.store_user(username)
                    answer = input("want to create another one? Type 'yes/no':  ")
            elif usr_input == 'ret':
                    storage.retr_user()



        elif init_input == 'pass':
            usr_input = input("Type 'gen' to generate pwd, 'ret' to retrieve pwd, or 'q' to exit program:  ")
            if usr_input == 'gen':
                answer = "yes"
                while answer == "yes":
                    pass_length = int(input("Enter the number of characters you need for your password: "))
                    urpd = generator.pass_gen(pass_length)
                    print("Your password is: ", urpd)
                    store = input("Would you like to save password 'y/n':  ")
                    if store == 'y':
                        storage.store_pass(urpd)
                    answer = input("want to create another one? Type 'yes/no':  ")
            elif usr_input == 'ret':
                storage.retr_pass()

        elif init_input != ('user' or 'pass'):
            print("Sorry try, again")

        init_input = input("Is this for uname ('user') or password ('pass')? Type 'q' to exit program:  ")

except Exception:
    print("Something went wrong.")

finally:
    print("Thanks for using our password manager!")
