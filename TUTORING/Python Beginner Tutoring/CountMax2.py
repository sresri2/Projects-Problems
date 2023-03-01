nums = [1,2,4,5,5,6,7,7,7,10,12,12]
target = 5

'''
.count()
.sort()
'''
nums.sort()
print("The Maximum is ",nums[-1])
count = nums.count(target)
print("The count of target in nums is ",count)

