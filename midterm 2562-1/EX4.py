print('Please select operation -')
print('1. Add')
print('2. Subtract')
print('3. Multiply')
print('4. Divide')
cho = int(input('Select operation form 1,2,3,4 : '))
first = int(input('Enter first number : '))
second = int(input('Enter second number : '))
if cho ==1 :
    total = (first+second)
    print(first,'+',second,'=',total)
elif cho ==2 :
    total = (first-second)
    print(first,'-',second,'=',total)
elif cho ==3 :
    total = (first*second)
    print(first,'*',second,'=',total)
else :
    total = (first/second)
    print(first,'/',second,'=',total)