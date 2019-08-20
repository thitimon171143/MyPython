z = 0
x = 0
average = float(input('Enter number : '))

while average >= 0 :
    z += average
    x += 1
    average = float(input('Enter number : '))
if x == 0 :
    print('No Data')
else :
    print('Average = ',(z/x))