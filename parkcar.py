import math
hrintime = int(input('Hour in : '))
minintime = int(input('Minute in : '))
hrouttime = int(input('Hour out : '))
minouttime = int(input('Minute out : '))

in_timemin = (hrintime*60)+minintime
out_timemin = (hrouttime*60)+minouttime

#cal
time_hr = hrouttime-hrintime
time_min = minouttime-minintime
summin= (time_hr*60)+time_min

#open
x = 0
if in_timemin<7*60 or in_timemin>23*60 :
    print("Can't in Cosed")
    x = 1
if out_timemin<7*60 or out_timemin>23*60 :
    print("Can't out Closed")
    x = 1

if x==0 :
    if summin <= 15:
        print('0')
    elif summin<=3*60:
        print(10*int(math.ceil(summin/60)))
    elif summin<=6*60:
        print(20*int(math.ceil(summin/60)))
    elif summin>6*60:
        print('200')
    else:
        'Error'
else:
    print('Pls new')
