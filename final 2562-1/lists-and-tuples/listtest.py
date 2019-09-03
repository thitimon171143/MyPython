def findBigestNum(nums):
    bigest = nums[0]
    for i in nums :
        if i > bigest :
            bigest = i
    return(bigest)

def findEven(nums):
    even = 0
    for i in nums :
        if i%2 == 0 :
            even += 1
    return even

listnum = [4,5,17,3,2,9,6]

print(findBigestNum(listnum))
print(max(listnum))
print(min(listnum))
print(findEven(listnum))