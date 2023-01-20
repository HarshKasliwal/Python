class Employee:
    empCount = 0
    def __init__(self, ID):
        self.set_emp_count() 
        self.ID = ID

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def get_id(self):
        return self.ID

    @classmethod
    def set_emp_count(cls):
        cls.empCount += 1
n = int(input('ENTER NUMBER OF EMPLOYEES: '))
emps = []
print('Enter the name of Employees: ')
for i in range(n):
    temp = Employee(i+1)
    emp_name = input()
    temp.set_name(emp_name)
    emps.append(temp)

print('\n\nTOTAL NO OF EMPLOYEES : {} \n\n'.format(Employee.empCount)) 
print('*************** DATA OF EMPLOYEES ***************\n') 
print('\tEmpoyee ID \t\t Employee Name')
for e in emps :
    print('	   {}\t\t	 {}'.format(e.ID, e.name))
