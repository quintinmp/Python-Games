from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open ("key.key" , "wb") as key_file:
        key_file.write(key)'''
        
# a function needs to defined before you use it
def load_key():
    file = open("key.key" , "rb")
    key = file.read()
    file.close()
    return key

key = load_key() 
fer = Fernet(key)


def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            #rstrip is used to remove the new line tag (\n)
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:", fer.decrypt(passw.encode()).decode())


def add():
    name = input('Account Name: ')
    pwd = input('Password: ')
# using with will automatically close file after operations are done as opposed to file which will not
    with open('passwords.txt', 'a') as f:
        # \n is used to start a new line
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


while True:
    mode = input("Would you like to add a new password or view existing ones (view, add)? Or press q to quit. ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue