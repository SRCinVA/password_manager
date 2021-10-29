master_pwd = input("What is the master password? ")

def view():# 'pass' just prevents indentation errors
    with open('passwords.txt', 'r') as f:   # 'with' opens the file, let's us complete tasks, and then closes that file automatically
                                            # 'r' is 'read mode' (we don't want to change it) 
                                            # 'as f' names that file ('f')
        for line in f.readlines():          # notice that readlines() is a method
            data = line.rstrip()            # oddly you have to 'rstrip' the carriage retun off of it.)
            user, passw = data.split("|")   # it splits a string everywhere that character is found and drops the pieces into a list.
                                            # the element of the list is assigned to user, while the second is assigned to passw.
            print("User:", user, "Password:", passw)             

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