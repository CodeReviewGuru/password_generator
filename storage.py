def store_pass(password):
    file = open('pwd.txt', 'a')
    file.write(password + '\n')
    file.close()
    print("Password was saved")

def retr_pass():
    file = open('pwd.txt', 'r')
    passwords = file.readlines()
    for items in passwords:
        print(items)
    file.close()
    print("*****End of File*****")

def store_user(username):
    file = open('usr.txt', 'a')
    file.write(username + '\n')
    file.close()
    print("Username was saved")

def retr_user():
    file = open('usr.txt', 'r')
    usrnames = file.readlines()
    for items in usrnames:
        print(items)
    file.close()
    print("*****End of File*****")