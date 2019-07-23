anoter = 'y'

while anoter == 'y' :
    wholesalecost = float(input("Enter the item's wholesale cost: "))
    retailprice = wholesalecost*2.5
    print('Retail price: $',format(retailprice ,'.1f'))
    anoter = input('Do you have anoter item? (Enter y for yes): ')