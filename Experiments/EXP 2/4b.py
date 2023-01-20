str1 = str(input("Enter the string : "))

str2 = reversed(str1)

if list(str1) == list(str2):
   print("The string is a palindrome.")
else:
   print("The string is not a palindrome.")