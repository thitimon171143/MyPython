hrintime = int(input('Hours In Time : '))
minintime = int(input('Minute In Time : '))
hrouttime = int(input('Hours Out Time : '))
minouttime = int(input('Minute Out Time : '))

hour=hrouttime-hrintime
min1=minouttime-minintime
min2=hour*60
total=min1+min2

if (hrintime<7 or hrintime>=24)or(hrouttime<7 or hrouttime>=24)or(hrouttime==23 and minouttime!=0)or(hrintime>=60 or minintime>=60):
    print('error')
elif total<=15:
    print('You must pay for 0 ')
elif total<60:
    print('You must pay for 10 ')
elif total<120:
    print('You must pay for 20 ')
elif total<=180:
    print('You must pay for 30 ')
elif total<240:
    print('You must pay for 50 ') 
elif total<300:
    print('You must pay for 70 ')
elif total<360:
    print('You must pay for 90 ')
elif total>360 and total<960:
    print('You must pay for 200')
else :
    print('error')