def main():
    sales_file = open('/Users/Python/Desktop/MyPython/final 2562-1/file-n-exceptions/sales.txt','r')
    for line in sales_file:
        amount = float(line)
        print(format(amount,'.2f'))
    sales_file.close()
main()