import array as s
a=s.array('i',[])
    
n=int(input("Length of the Array is??? "))
for i in range(0,n):
    a.append(int(input("Element {}: ".format(i+1))))

b=int(input("Enter the element to be appended : "))
a.append(b)
print(a)