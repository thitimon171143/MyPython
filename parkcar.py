hrintime = int(input('Hour in : '))
minintime = int(input('Minute in : '))
hrouttime = int(input('Hour out : '))
minouttime = int(input('Minute out : '))
if hrintime==0 and minintime <=15 :
    price = ('0')
elif hrintime<=3 and minintime>=16 :
    price = ('10')
elif hrintime>=4 and minintime>=16 :
    price = ('20')
elif hrintime>=6 and minintime>=16 :
    price = ('200')
print('Total : ',price)