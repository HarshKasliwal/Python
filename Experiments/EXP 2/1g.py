import array as s
import array as s
a=s.array('i',[])
n=int(input("Length of the array is: "))

for i in range(0,n):
    a.append(int(input("Element {}:  ".format(i+1))))
print(a)

m=int(input("Enter the element to be inserted: "))
p=int(input("Enter the index to be located: "))

a.insert(p,m)
print(a)