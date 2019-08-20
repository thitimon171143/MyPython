test = input('Enter a string: ')
print('This is what I found about that string:')

if test.isalnum() :
    print('The string is alphanumeric.')
if test.isalpha() :
    print('The string contains only alphabetic characters.')
if test.islower() :
    print('The letter in the string are all lowercase.')
if test.isnumeric() :
    print('The string contains only digits.')
if test.isupper() :
    print('The letters in the string are all uppercase.')