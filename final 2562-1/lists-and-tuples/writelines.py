def main():
    cities = ['New York','Boston','Atlanta','Dallas']
    outfile = open('/Users/Python/Desktop/MyPython/final 2562-1/lists-and-tuples/cities.txt','w')
    cities = map(lambda x: x+'\n',cities)
    outfile.writelines(cities)
    outfile.close
main()