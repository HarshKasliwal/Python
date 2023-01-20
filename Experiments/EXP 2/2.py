import array as s
import array as s
a=s.array('i',[])
b=s.array('i',[])
n=int(input("Length of the array is: "))

for i in range(0,n):
    a.append(int(input("Element {}:  ".format(i+1))))
b.append(2)

for i in a:
    for j in range(2,i):
        if(i % j==0):
            break
        if(j==i-1):
            b.append(i)

for j in b:
    while j in a:
        a.remove(j)
print(a)