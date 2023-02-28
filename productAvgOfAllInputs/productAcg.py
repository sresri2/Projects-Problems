nums = []
num = input("Enter your integer here. Q to quit: ")
while num != 'q' and num != 'Q':
    nums.append(int(num))
    print("Enter your integer below, or type q to quit!")
    num = input("Enter your integer here: ")

if len(nums) == 0:
    print("The Product and Average are both 0")
product = 1.0
for i in nums:
    product *= i

print("The Product is ",product)
sum = 0.0
for i in nums:
    sum += i

avg = sum/float(len(nums))
print("The average is ",avg)