import os
def main():
    old = input('Enter old message : ')
    new = input('Enter new message : ')
    infile = open('/Users/Python/Desktop/MyPython/final 2562-1/file-n-exceptions/employees2.txt','r')
    outfile = open('/Users/Python/Desktop/MyPython/final 2562-1/file-n-exceptions/Temp.txt','w')
    for line in infile:
        rec = (line.rsplit('|'))
        if rec[0] == old :
            outfile.write(new+'|'+rec[1]+'|'+rec[2])
        else:
            outfile.write(line)
    infile.close()
    outfile.close()

    os.remove('/Users/Python/Desktop/MyPython/final 2562-1/file-n-exceptions/employees2.txt')
    os.rename('/Users/Python/Desktop/MyPython/final 2562-1/file-n-exceptions/Temp.txt','/Users/Python/Desktop/MyPython/final 2562-1/file-n-exceptions/employees2.txt')

main()