sum = 0.0
product = 1.0
count = 0.0
num = input("Enter your integer here. Q to quit: ")

while num != 'q' and num != 'Q':
    product *= int(num)
    sum += int(num)
    count += 1
    num = input("Enter your integer here. Q to quit: ")

if count == 0:
    print("The Product is 0")
    print("The Average is 0")
    quit()

print("The Product is ",product)
print("The Average is ", sum/count)