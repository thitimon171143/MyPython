total = 0
number = int(input('Enter Number : '))

for i in range(number):
    if i%3 ==0 or i%5 ==0 :
        total = total+i
print(total)
