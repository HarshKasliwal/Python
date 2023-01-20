import re
lst = []

with open('phonebook.txt', 'r') as my_file:
    for entry in my_file:
        lst.append(entry.split())

print("The entries in the phonebook are : ")
for contact in lst:
    print(contact)
print("The entries with rao as surname are : ")
for contact in lst:
    check = re.search('rao', contact[0])
    if check:
        print(contact)

print("The entries with first name starting with J or K are :")
for contact in lst:
    check = re.search('(^j)|(^k)', contact[1].lower())
    if check:
        print(contact)
