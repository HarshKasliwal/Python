class Person :
    def __init__(self, height) : 
        self.height = height

    def __ge__(self, other) :
        return self.height >= other.height
h1 = int(input('Enter the height of 1st person: ')) 
h2 = int(input('Enter the height of 2nd person: '))
 
p1 = Person(h1)
p2 = Person(h2)
 
if(p1 >= p2) :
    print('First person is Taller ! ') 
else :
    print('Second person is Taller ! ')
