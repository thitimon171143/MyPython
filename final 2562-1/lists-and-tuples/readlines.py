def main():
    infile = open('/Users/Python/Desktop/MyPython/final 2562-1/lists-and-tuples/cities.txt','r')
    cities = infile.readline()
    infile.close()
    index = 0
    while index < len(cities):
        cities[index] = cities[index].rstrip('\n')
        index += 1
    print(cities)
main()