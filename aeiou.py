word = input("Enter your word : ")
vowel = ['a','u','i','o','e']
n = 0
i = 0
up= 0
num = 0

len_in = len(word)
len_Te = len(vowel)

for i in range(len_in) :
    for ii in range(len_Te) :
        if word[i] in vowel[ii]:
            n = 1
    if n == 1 and up == 0:
        num += 1
        up = 1
    elif n == 0 :
        up = 0
    n = 0
print('Your vowel is',num)