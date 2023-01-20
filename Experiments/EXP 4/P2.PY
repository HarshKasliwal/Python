def accept():
    lst = []
    while(True):
        print("Enter '!' to stop. Enter '!!' to enter details of a new student")
        n = input()
        if n == '!':
            break
        lst.append((input("Enter name of student : "),
                    input("Enter roll no : "),
                    int(input("Enter marks in subject 1 : ")),
                    int(input("Enter marks in subject 2 : ")),
                    int(input("Enter marks in subject 3 : "))))
    return lst


def display_student(student):
    print("Name of student :", student[0])
    print("Roll no of student:", student[1])
    print("Marks in subjecct 1:", student[2])
    print("Marks in subject 2:", student[3])
    print("Marks in subject 3:", student[4])
    print("Total marks :", student[2]+student[3]+student[4])
    print()


def display_all():
    global lst
    for student in lst:
        display_student(student)


def display(name):
    global lst
    for student in lst:
        if student[0] == name:
            display_student(student)


while(True):
    global lst
    print("\n1-Input details of students\n2-Display details of all students\n3-Display details of student whose name is X\n4-Exit")
    ch = int(input("Enter your choice : "))
    if ch == 1:
        lst = accept()
    elif ch == 2:
        display_all()
    elif ch == 3:
        name = input("Enter student's name : ")
        display(name)
    else:
        break