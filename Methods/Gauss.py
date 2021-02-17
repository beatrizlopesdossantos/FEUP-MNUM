matrix = [[1, 0.5,1/3, -1],
          [1/2, 1/3, 1/4, 1],
          [1/3, 1/4, 1/5, 1]]

def rowOp(down, up, k):
    global matrix
    for p in range(len(matrix[0])):
        matrix[down][p] -= k * matrix[up][p]


def gauss():
    global matrix
    for i in range(len(matrix)):
        rowOp(i, i, (1 - 1 / matrix[i][i]))
        for j in range(i, len(matrix)):
            if i != j:
                rowOp(j, i, matrix[j][i])


gauss()
for i in matrix:
    print(i)
    
