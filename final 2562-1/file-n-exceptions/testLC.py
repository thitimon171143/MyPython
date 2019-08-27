def main():
    infileA = open('/Users/Python/Desktop/MyPython/final 2562-1/file-n-exceptions/LA.txt','r')
    infileB = open('/Users/Python/Desktop/MyPython/final 2562-1/file-n-exceptions/LB.txt','r')
    outfileC = open('/Users/Python/Desktop/MyPython/final 2562-1/file-n-exceptions/LC.txt','w')

    for line1 in infileA :
        numa = float(line1)
        print(format(numa,'.2f'))
        numb = float(infileB.readline())
        print(format(numb,'.2f'))
        numc = numa+numb
        outfileC.write(str(numc)+'\n')
    
    infileA.close()
    infileB.close()
    outfileC.close()
main()