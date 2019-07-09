print('Please select operation -')
print('1. Add')
print('2. Subtract')
print('3. Multiply')
print('4. Divide')
cho = int(input('Select operation form 1,2,3,4 : '))
first = int(input('Enter first number : '))
second = int(input('Enter second number : '))
if cho ==1 :
    print(first,'+',second,'=',first+second)
elif cho ==2 :
    print(first,'-',second,'=',first-second)
elif cho ==3 :
    print(first,'*',second,'=',first*second)
else :
    print(first,'/',second,'=',first/second)