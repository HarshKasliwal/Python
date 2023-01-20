def perfect_num(n):
    sum=0
    for i in range(1,n):
        if(n % i ==0):
            sum = sum + i
    if(sum == n):
        print("%d is a perfect number" %n)
    else:
        print("%d is not a perfect number" %n)
num = int(input("Enter the number:"))
perfect_num(num)