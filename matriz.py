def flippingMatrix(matrix):
    n = len(matrix)//2
    total = 0
    for i in range(n):
        for j in range(n):
            total += max(matrix[i][j], 
            matrix[i][2*n - 1 - j], 
            matrix[2*n - 1 - i][j], 
            matrix[2*n - 1 - i][ 2*n - 1-j])
    return total

matriz = [
    [1,  2,  3,  4,  5,  6],
    [7,  8,  9, 10, 11, 12],
    [13,14, 15,16, 17, 18],
    [19,20, 21,22, 23, 24],
    [25,26, 27,28, 29, 30],
    [31,32, 33,34, 35, 36]
]
print(flippingMatrix(matriz))