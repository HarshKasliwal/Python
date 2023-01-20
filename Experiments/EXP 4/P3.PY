def accept():
    st = set()
    print("Enter your elements. Enter '!' to stop")
    while(True):
        n = input()
        if n == '!':
            break
        st.add(int(n))
    return st


print("Enter set A")
A = accept()
print("Enter set B")
B = accept()
while(True):
    print("\n1-Print sets\n2-Intersection\n3-Union\n4-Difference\n5-Symmetric difference\n6-Exit")
    choice = int(input("Enter your choice : "))
    if(choice == 1):
        print("Set A: ", A)
        print("Set B: ", B)
    elif choice == 2:
        print("The intersection is :", A & B)
    elif choice == 3:
        print("The union is :", A | B)
    elif choice == 4:
        print("The difference is:", A-B)
    elif choice == 5:
        print("The symmetric difference is:", A ^ B)
    else:
        break
