s = 0
n = 0
while True :
    t = float(input())
    if t < 0 : break
    s += t
    n += 1
if n == 0 :
     print('No Data')
else:
    print('avg =',(s/n))