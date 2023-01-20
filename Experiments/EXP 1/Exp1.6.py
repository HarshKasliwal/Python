
# ********Pyramid using stars**********\

size = 5
m = size
for i in range(0, size):
    for j in range(0, m):
        print(end=" ")
    m = m - 1 # decrementing m after each loop
    for j in range(0, i + 1):
        
        # printing full Triangle pyramid using stars
        
        print("* ", end=' ')
    print(" ")


'''
# Downward triangle using stars
size = 5

k = size

for i in range(size, -1, -1):

    for j in range(k, 0, -1):
        print(end=" ")
    
    for j in range(0, i):

        print("*", end=" ")

    print(" ")'''

'''
# Triangle using alphabet
size = 5

ascii_value = 65

for i in range(size):
    for j in range(i+1):
        alphabet = chr(ascii_value)
        print(alphabet, end=" ")
    
    ascii_value += 1
    print(" ")
'''
'''
size = 5
for i in range(1,size+1):
    for j in range(1, size+1-i):
        print(' ', end=' ')
    for j in range(1,i+1):
        print(j, end=' ')
    for j in range(i-1,0,-1):
        print(j, end=' ')
    print()
    '''