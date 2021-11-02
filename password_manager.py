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
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key   # to make the key available to outside the function

master_pwd = input("What is the master password? ")
key = load_key() + master_pwd.encode() # for reasons he doesn't explain, key and fer need to come after master_pwd
                                    # we'll be storing this in bytes (using .encode()) and then concatenate the two strings
fer = Fernet(key)                   # this initiaizes the encryption module

def view():# 'pass' just prevents indentation errors
    with open('passwords.txt', 'r') as f:   # 'with' opens the file, let's us complete tasks, and then closes that file automatically
                                            # 'r' is 'read mode' (we don't want to change it) 
                                            # 'as f' names that file ('f')
        for line in f.readlines():          # notice that readlines() is a method
            data = line.rstrip()            # oddly you have to 'rstrip' the carriage retun off of it.)
            user, passw = data.split("|")   # it splits a string everywhere that character is found and drops the pieces into a list.
                                            # the element of the list is assigned to user, while the second is assigned to passw.
            print("User:", user, "| Password:", 
                fer.decrypt(passw.encode()).decode()) # first we encode that string into bits, then decrypt it.          
                                            # strangely, outside the print statement you decode it so it takes away the bit ('b' designation)
def add():
    name = input("Account Name: ")
    pwd = input("Password: ")
    
    with open('passwords.txt', 'a') as f:   # 'with' opens the file, let's us complete tasks, and then closes that file automatically
                                            # 'a' is 'append mode' (other are 'w' and 'r') 
                                            # 'as f' names that file ('f')
        # when writing passwords, they are encoded first and then encrypted (notice the 'fer.' prefix). Convert it all to a string.
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + '\n')    # add a line break
                                                                           # this weird 'decode()' converts it from "bit string" 
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