from cryptography.fernet import Fernet as ft
#"abdullah@gmail.com", "Hassan@gmail.com"
#"123@#", "Ha55an"
emails = []
passwords = []

def main():
    
    key = input("Enter the key : ")
    fileKey = loadKey()
    key = fileKey + key.encode()
    fer = ft(key)
    # add()
    load(fer)
    view()
    store(fer)
    
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
    
def store(fer):
    file = open("data.txt", 'w')
    for i in range(0, len(emails)):
        file.write(emails[i] + "," + str(fer.encrypt(passwords[i].encode())) + "\n")
    file.close()
    
def parse(line):
    line = line.split(',')
    print(line)
    if(line != ''):
        return line[0], line[1]
    else:
        return 0

def load(fer):
    file = open("data.txt", 'r')
    data = file.read().split('\n')
    print(data)
    for i in data:
        if(i != data[-1]):
            line1, line2 = parse(i)
            emails.append(line1)
            passwords.append(fer.decrypt(line2.encode()).decode())
    file.close()
    

main()