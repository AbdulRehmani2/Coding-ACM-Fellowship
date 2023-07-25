import os.path
#"abdullah@gmail.com", "Hassan@gmail.com"
#"123@#", "Ha55an"
emails = []
passwords = []

def main():
    # key = input("Enter the key : ")
    # add()
    load()
    view()
    # store()
    
    
    
def view():
    for i in range(0, len(emails)):
        print(f"Email : {emails[i]} || Password : {passwords[i]}")
        
def add():
    email = input("Enter the email : ")
    password = input("Enter the password : ")
    emails.append(email)
    passwords.append(password)
    
def store():
    file = open("data.txt", 'w')
    for i in range(0, len(emails)):
        file.write(emails[i] + "," + passwords[i] + "\n")
    file.close()
    
def parse(line):
    line = line.split(',')
    print(line)
    if(line != ''):
        return line[0], line[1]
    else:
        return 0

def load():
    file = open("data.txt", 'r')
    data = file.read().split('\n')
    print(data)
    for i in data:
        if(i != data[-1]):
            line1, line2 = parse(i)
            emails.append(line1)
            passwords.append(line2)
    file.close()
    

main()