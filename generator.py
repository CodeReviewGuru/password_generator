import random
import string

def pass_gen(pwd_length):
    opt_list = string.ascii_letters + string.punctuation + string.digits
    password = " "
    for item in range(0, pwd_length):
        item = random.choice(opt_list)
        password = password + item
    return password

def user_gen():
    opt_list = string.ascii_letters
    user_name = " "
    for item in range(8):
        item = random.choice(opt_list)
        user_name = user_name + item
    return user_name
