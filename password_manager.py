master_pwd = input("What is the master password? ")

def view():
    pass # this just prevetns indentation errors

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")
    
    with open('passwords.txt', 'a') as f:   # 'with' opens the file, let's us complete tasks, and then closes that file automatically
                                            # 'a' is 'append mode' (other are 'w' and 'r') 
                                            # 'as f' names that file ('f')
        f.write(name + "|" + pwd)

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