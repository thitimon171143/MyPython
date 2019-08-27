def main():
    num_emps = int(input('How many employee records '+\
                        'do you want to create?'))
    emp_file = open('/Users/Python/Desktop/MyPython/final 2562-1/file-n-exceptions/employees2.txt','w')
    for count in range(1,num_emps+1):
        print('Enter data for employee #',count,sep='')
        name = input('Name : ')
        id_num = input('ID Number : ')
        dept = input('Department : ')
        emp_file.write(name+'|'+id_num+'|'+dept+'\n')
        print()
    emp_file.close()
    print('Employee records written to employees.txt')
main()