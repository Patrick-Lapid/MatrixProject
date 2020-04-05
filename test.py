def add(matrix1, matrix2, rowlength):
    matrix3 = []
    x = 0
    while x < rowlength:
        matrix3.append(matrix1[x] + matrix2[x])
        x += 1
    print(matrix3)

def subtract(matrix1, matrix2, length):
    matrix3 = []
    x = 0
    while x < length:
        matrix3.append(matrix2[x] - matrix1[x])
        x += 1
    print(matrix3)
