first = input('Enter your first name : ')
last = input('Enter your last name : ')
idnum = input('Enter your student ID number : ')
f = first[0:3]
l = last[0:3]
i = idnum[-3:]

print('Your system login name is :')
print(str(f)+str(l)+str(i))