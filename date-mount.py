date_string = '06/26/2014'
date_list = date_string.split('/')

print('Month:',date_list[0])
print('Day:',date_list[1])
print('Year:',date_list[2])
print(date_list)

if date_list[0] == '01' :
    print(date_list[1]+' January '+date_list[2])
elif date_list[0] == '02' :
    print(date_list[1]+' February'+date_list[2])
elif date_list[0] == '03' :
    print(date_list[1]+' March '+date_list[2])
elif date_list[0] == '04' :
    print(date_list[1]+' April '+date_list[2])
elif date_list[0] == '05' :
    print(date_list[1]+' May '+date_list[2])
elif date_list[0] == '06' :
    print(date_list[1]+' June '+date_list[2])
elif date_list[0] == '07' :
   print(date_list[1]+' July '+date_list[2])
elif date_list[0] == '08' :
    print(date_list[1]+' August '+date_list[2])
elif date_list[0] == '09' :
    print(date_list[1]+' September '+date_list[2])
elif date_list[0] == '10' :
    print(date_list[1]+' October '+date_list[2])
elif date_list[0] == '11' :
    print(date_list[1]+' Noverber '+date_list[2])
elif date_list[0] == '12' :
    print(date_list[1]+' December '+date_list[2])
else :
    print('Error')