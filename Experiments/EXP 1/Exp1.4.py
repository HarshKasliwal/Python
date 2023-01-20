for n in range(1, 1001, 1):
    sum = 0
    x = n
    while x!=0:
        r = x%10
        sum = sum + r ** 3
        x = x//10

    if n == sum:
        print(n)
