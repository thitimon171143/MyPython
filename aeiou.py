sentence = input('Enter word : ')
count = 0

for x in sentence :
    if x in 'aeiou' :
        count += 1

print(count)