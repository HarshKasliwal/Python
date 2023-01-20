import array as s
a=s.array('i',[])
n=int(input("Length of the array is : "))

for i in range(0,n):
    a.append(int(input("Element {}:  ".format(i+1))))

print(a)