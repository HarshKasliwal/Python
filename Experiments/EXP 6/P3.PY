class Customer:

    def __init__(self, ID, name, mobile_num): 
        self.ID = ID
        self.name = name 
        self.mobile_num = mobile_num


    def add_content_to_file(self):
        with open("Details.txt", 'a') as f: 
            f.write(f"{self.ID}, {self.name}, {self.mobile_num}\n")

    @classmethod
    def print_content_of_file(cls):
        with open("Details.txt", 'r') as f: 
            file_content = f.read()
            print("\nThe file content:\n" + ("-" * 30) + f"\n{file_content}" +("-" * 30))
    
n = int(input('ENTER NUMBER OF CUSTOMERS: '))

for i in range(n) :
    customer_name = input('\nEnter customer name: ') 
    customer_number = input('Enter customer number: ')

    # Creating n Customer Instances
    customer_instance = Customer(i + 1, customer_name, customer_number)

    # Appending content to file 
    customer_instance.add_content_to_file()

    # Print final content of the file 
Customer.print_content_of_file()
