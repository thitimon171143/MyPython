big = input('Enter sentence : ')
count = 0
for x  in big:
    if x.isupper():
        count += 1
print(count)
