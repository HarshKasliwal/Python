def accept():
    lst = []
    print("Enter your elements.\nTo stop enter '!'")
    while(True):
        n = input()
        if n == '!':
            break
        lst.append(int(n))
    return lst


lst = []
while(True):
    print("\n1-Separate Even and Odd elements\n2-Merge and sort list\n3-Update the first element\n4-Print middle element\n5-Exit")
    ch = int(input("Enter your choice : "))
    if ch == 1:
        print("Enter your list")
        lst = accept()
        even_lst, odd_lst = [], []
        for n in lst:
            if n % 2 == 0:
                even_lst.append(n)
            else:
                odd_lst.append(n)

        print("Even list :", even_lst)
        print("Odd list :", odd_lst)
    elif ch == 2:
        print("Enter list 1")
        lst1 = accept()
        print("Enter list 2")
        lst2 = accept()
        lst = lst1+lst2
        lst.sort()
        print("After merging and sorting, lists become :", lst)
    elif ch == 3:
        print("Enter list")
        lst = accept()
        n = int(input("Enter element : "))
        lst[0] = n
        print("List with first element updated is :", lst)
    elif ch == 4:
        print("Enter list")
        lst = accept()
        if len(lst) % 2 == 0:
            print("Middle elements of list are : ", lst[len(lst)//2-1],
                  lst[len(lst)//2])
        else:
            print("Middle element of list is :", lst[len(lst)//2])
    else:
        break 
