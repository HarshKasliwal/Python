n = int(input("How many terms ?: "))
first=0
second=1
i=0
if n<=0:
    print("Please enter a positive integer")
elif n==1:
    print("Fibonacci sequence upto",n,":")
    print(first)
else:
    print("Fibonacci sequence: ")
    while n>i:
        print(first)
        next = first + second
        first = second
        second = next
        i += 1
