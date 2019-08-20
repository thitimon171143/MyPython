hourswork = int(input('Enter the number hours worked: '))
payrate = int(input('Enter the hourly pay rate: '))

if hourswork > 40 :
    gross = (hourswork-40)*(payrate*1.5)+(40*payrate)
else :
    gross = hourswork*payrate
print('The gross pay is ',gross)