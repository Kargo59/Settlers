import random

#print(random.randrange(0,2))

def create_matrix(n,i,j):
    if i > n or j > n:
        print("i or j out of range, changing i and j to 0")
        i = 0
        j = 0

    #create the matrix given the variable n
    global matrix
    secondary = 2
    secondary = n
    matrix = []
    while n > 0:
        matrix.append([])
        n -=1
    for x in range(secondary):
        for y in range(secondary):
            matrix[y].append(random.randrange(0,2))
    #an element of the matrix cant connect to itself
    for a in range(len(matrix)):
        matrix[a][a] = 0


    print(matrix)
    #print(secondary)
    print(*matrix, sep='\n')

    if matrix[i][j] == 1:
        print('True')
    else:
        print('False')



create_matrix(9,4,7)



