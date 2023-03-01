'''
nums = []
target = 5

count of target in nums
    how many times target occurs in nums

maximum number in nums
'''

nums = [1,2,4,5,5,6,7,7,7,10,12,12]
target = 5

mmax = nums[0]
count = 0
for i in nums:
    if i > mmax:
        mmax = i
    if i == target:
        count += 1

print("The Maximum was ",mmax)
print("The count of target was ",count)
    

    




