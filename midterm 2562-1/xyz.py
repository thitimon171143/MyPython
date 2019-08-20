n = 20
for x in range(1,n):
    for y in range(x,n):
        t = x**2 + y**2
        z = int(round(t**(1/3),0))

        if z**3 == t :
            print(z,x,y)