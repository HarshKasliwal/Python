def accept():
    dct = {}
    while(True):
        print("Enter '!' to stop. Enter '!!' to enter new key/value pair")
        n = input()
        if n == '!':
            break
        key = input("Enter key : ")
        value = input("Enter value : ")
        dct[key] = value
    return dct


print("Enter dictionary pairs")
dct = accept()
while(True):
    print("\nEnter the choice: \n1:Print dictionary \n2:Sort by key \n3:Concatenate\n4:Exit")
    choice = int(input())
    if choice == 1:
        print("The dictionary is: ",  dct)
    elif choice == 2:
        print("The dictionary sorted by key is:", sorted(dct.items()))
    elif choice == 3:
        print("Enter second dictionary")
        dct2 = accept()
        dct_conc = dct.copy()
        dct_conc.update(dct2)
        print("Concatenated dictionary is:", dct_conc)
    else:
        break
