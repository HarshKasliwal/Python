def add(*num):
    sum = 0
    for num in nums:
        sum =num + sum 
    return sum

def sub(*num):
    sum = 0
    for num in nums:
        sum=num-sum
        
    return sum

def mul(*num):
    prod = 1
    for num in nums:
        prod =num * prod 
    return prod

ch = int(input("1. Addition\n2. Subtraction\n3. Multiplication\n\nEnter your choice: "))
print("To stop entering numbers enter '!'")

nums = []
while True:
    n=input()
    if n =='!':
        break
    else:
        nums.append(int(n))
        
if ch==1:
    print("Sum of entered numbers is {}".format(add(*nums)))
elif ch==2:
    print("Subtraction of entered numbers is {}".format(sub(*nums)))
elif ch==3:
    print("Multiplication of entered numbers is {}".format(mul(*nums)))