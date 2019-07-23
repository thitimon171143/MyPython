s = 0
n = 0
t = float(input())
while t >= 0 :
    t = float(input())
    s += t
    n += 1
if n == 0 :
     print('No Data')
else:
    print('avg =',(s/n))