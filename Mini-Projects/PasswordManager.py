from cryptography.fernet import Fernet as ft

emails = []
passwords = []

def main():
    key = input("Enter the key : ")
    fileKey = loadKey()
    key = fileKey + key.encode()
    fer = ft(key)
    load(fer)
    while(True):
        choice = int(input("1. Add new password\n2. Show all passwords\n"))
        if(choice == 1):
            add()
        elif(choice == 2):
            view()
    
def loadKey():
    file = open("key.key", 'rb')
    key = file.read()
    file.close()
    return key
    
def view():
    for i in range(0, len(emails)):
        print(f"Email : {emails[i]} || Password : {passwords[i]}")
        
def add():
    email = input("Enter the email : ")
    password = input("Enter the password : ")
    emails.append(email)
    passwords.append(password)
    file = open("data.txt", 'a')
    file.write(email + "," + fer.encrypt(password.encode()).decode() + "\n")
    file.close()
    
def parse(line):
    line = line.split(',')
    if(line != ''):
        return line[0], line[1]
    else:
        return 0

def load(fer):
    file = open("data.txt", 'r')
    data = file.read().split('\n')
    for i in data:
        if(i != data[-1]):
            line1, line2 = parse(i)
            emails.append(line1)
            passwords.append(fer.decrypt(line2.encode()).decode())
    file.close()
    

main()