a = str(input("Enter the string: "))
print("The original string is: " + a)
b = a[0] + a[1:].replace(a[0], '@')
print("Replaced String: " + str(b))