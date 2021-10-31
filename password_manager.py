from cryptography.fernet import Fernet

'''  
# you just need to run this once to get the key
 # also, a multi-line comment is three quote marks

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:  # 'wb' means "write bytes"
        key_file.write(key)
'''
# now we need to load the key first, because we're going to call the fucntion directly below it.
def load_key():
    file = open("key.key", "rb").read()
    key file.read()
    file.close()
    return key   # to make the key available to outside the function

master_pwd = input("What is the master password? ")
key = load_key() + master_pwd.bytes # for reasons he doesn't explain, key and fer need to come after master_pwd
                                    # we'll be storing this in bytes and then concatenate the two strings
fer = Fernet(key)                   # this initiaizes the encryption module

def view():# 'pass' just prevents indentation errors
    with open('passwords.txt', 'r') as f:   # 'with' opens the file, let's us complete tasks, and then closes that file automatically
                                            # 'r' is 'read mode' (we don't want to change it) 
                                            # 'as f' names that file ('f')
        for line in f.readlines():          # notice that readlines() is a method
            data = line.rstrip()            # oddly you have to 'rstrip' the carriage retun off of it.)
            user, passw = data.split("|")   # it splits a string everywhere that character is found and drops the pieces into a list.
                                            # the element of the list is assigned to user, while the second is assigned to passw.
            print("User:", user, "| Password:", passw)             

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")
    
    with open('passwords.txt', 'a') as f:   # 'with' opens the file, let's us complete tasks, and then closes that file automatically
                                            # 'a' is 'append mode' (other are 'w' and 'r') 
                                            # 'as f' names that file ('f')
        f.write(name + "|" + pwd + '\n')    # add a line break

while True:
    mode = input("Would you like to add a new password or view existing ones ('view' or 'add'). Press 'q' to quit: ").lower()
    
    if mode == "q":
        print("Very well, we'll stop the program!")
        break

    if mode == "view":
        view()
    
    elif mode == "add":
        add()
    
    else:
        print("Invalid mode.")
    
    continue # to go back to the top of the while loop