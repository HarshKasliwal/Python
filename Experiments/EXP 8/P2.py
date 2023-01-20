import re

s = '''Mumbai Dubai Pune Aurangabad Chennai Indore Surat Jaipur Jalna Ambad Banglore Lucknow Dalai Kolkata Manglore Madukarai'''
cities = s.split()
print("Cities ending in ai are : ")
for city in cities:
    check = re.search('ai$', city)
    if check:
        print(city)

print("Cities starting with 'Mu' or 'Ma' are : ")
for city in cities:
    check = re.search('(^mu)|(^ma)', city.lower())
    if check:
        print(city)

print("Cities with 'u' as second letter and 'a' as second last letter are : ")
for city in cities:
    check = re.search('(^.u).*(a.$)', city.lower())
    if check:
        print(city)
