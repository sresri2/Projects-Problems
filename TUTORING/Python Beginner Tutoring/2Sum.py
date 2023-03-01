'''
nums = [1,2,3,4,5,6,7,8,9]
target = 6

pos = 0
for loop
    pos2 = pos + 1
    for loop[pos2:]
        if (the numbers add to target):
            print them out


'''

pos1 = 0
nums = [1,2,3,4,5,6,7]
target = 0
for i in nums:
    pos2 = pos1 + 1
    for j in nums[pos2:]:
        if nums[pos1]+nums[pos2] == target:
            print(nums[pos1],"+",nums[pos2])
            quit()
        pos2 += 1
    pos1 += 1
print("No numbers add to target value")
