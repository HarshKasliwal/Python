import array as s
a=s.array('i',[])
b=s.array('i',[])
n=int(input("Length of the array is : "))

for i in range(0,n):
    a.append(int(input("Element {}:  ".format(i+1))))

m=int(input("Length of the array is: "))
for i in range(0,m):
    b.append(int(input("Element {}:  ".format(i+1))))

for i in b:
    a.append(i)
print(a)