import pickle
def menu():
    again = 'y'
    while again == 'y' or again == 'Y' :
        print('-'*50)
        print("1. Look up a person's email address")
        print('2. Add a new name and email address')
        print('3. Change an existing email address')
        print('4. Delete an existing name and email address')
        print('-'*50)
        choose = int(input('Choose 1-4 : '))
        if choose == 1 :
            search()
        elif choose == 2 :
            add()
        elif choose == 3 :
            change()
        elif choose == 4 :
            delete()
        again = input('Enter more data? (y/n): ')

def search():
    infile = open('/Users/Python/Desktop/MyPython/final 2562-1/practice/per_mail.dat','rb')
    name = input('Input your name : ')
    if name in infile :
        print(infile[name])
    else:
        print(name,'not found')
def add():
    infile = open('/Users/Python/Desktop/MyPython/final 2562-1/practice/per_mail.dat','wb')
    per_email = {}
    per_email['name'] = input('Input your Name : ')
    per_email['email'] = input('Input your Email : ')
    infile.write(per_email)
    infile.close()

def change():
    infile = open('/Users/Python/Desktop/MyPython/final 2562-1/practice/per_mail.dat','rb')
    name = input('Input name : ')
    email = input('Input new email : ')
    infile[name] = email


def delete():
    name = input('Input name for delete : ')
    email = input('Input email for delete : ')


menu()