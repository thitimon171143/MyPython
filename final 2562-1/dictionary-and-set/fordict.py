phonebook = {'Anirach':'777-1111','Mickey':'777-2222','Donald':'777-3333'}
phonebook['Bart'] = [1,3,5]
elements = len(phonebook)
print('There are ',elements,' names in phonebook')
for key in phonebook:
    print(key,'phone number is :',phonebook[key])
phonebook['Bart'][1] = 9
print(phonebook)

print()
for i in list(phonebook)[::-1]:
    print(i,'phone number is :',phonebook[i])