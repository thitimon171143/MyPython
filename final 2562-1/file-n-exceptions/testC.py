def main():
    newfile = open('/Users/Python/Desktop/MyPython/final 2562-1/file-n-exceptions/A.txt','r')
    infile = open('/Users/Python/Desktop/MyPython/final 2562-1/file-n-exceptions/B.txt','r')
    outfile = open('/Users/Python/Desktop/MyPython/final 2562-1/file-n-exceptions/C.txt','w')

    out1 = int(infile.readline())
    out2 = int(infile.readline())
    out3 = int(infile.readline())
    out4 = int(infile.readline())

    out5 = int(newfile.readline())
    out6 = int(newfile.readline())
    out7 = int(newfile.readline())
    out8 = int(newfile.readline())

    outfile.write(str(out1+out5)+'\n')
    outfile.write(str(out2+out6)+'\n')
    outfile.write(str(out3+out7)+'\n')
    outfile.write(str(out4+out8)+'\n')

    outfile.close()
    infile.close()
    infile.close()
main()