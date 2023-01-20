name = input('What is your name: ')
age = int(input('How old are you: '))
#Using str.format()
str = "Your name is '{}' and you are'{}' years old."
out = str.format(name, age)
print(out)
#Using % operator
print("Your name is %s and your age is %d"%(name,age))

