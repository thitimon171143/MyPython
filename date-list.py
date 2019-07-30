date_string = input('Enter Date : ')
date_list = date_string.split('/')

print('Month:',date_list[0])
print('Day:',date_list[1])
print('Year:',date_list[2])
print(date_list)

mounth = ['January','February','March','April','May','June','July','August','September','October','Noverber','December']

print(mounth[int(date_list[0])-1])
