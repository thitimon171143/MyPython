def main():
    sales_file = open('/Users/Python/Desktop/MyPython/final 2562-1/file-n-exceptions/sales.txt','r')
    line = sales_file.readline()
    while line != '':
        amount = float(line)
        print(format(amount,'.2f'))
        line = sales_file.readline()
    sales_file.close()
main()