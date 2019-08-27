def main():
    count = 1
    infile = open('/Users/Python/Desktop/MyPython/final 2562-1/file-n-exceptions/employees.txt','r')
    for emp in infile:
        if (count == 1) :
            print('Name:'+emp.rstrip('\n'))
        elif (count == 2) :
            print('ID:'+emp.rstrip('\n'))
        elif (count == 3) :
            print('Dept:'+emp.rstrip('\n'))
            count = 0
        count += 1
    infile.close()
main()