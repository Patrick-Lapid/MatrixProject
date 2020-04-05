def introduction():
    print("Welcome! This is a matrix operation program where you enter two matrices via rows of columns and decide whether you would like to add subtract or multiply them.")
    print("\n"+"To enter a matrix, please use the format a, b, c, ... where each letter is a real number.")
    print("To enter a single column for a row, make sure to follow it up with a comma and to end with the number of rows. When you are satisfied with the number of rows you have, simply enter quit with a following comma if your matrix contains more than one column")
    print("For matrices with only one column, simply enter a row with a different number of columns to end matrix input")
    main()

firstMatrix = []
secondMatrix = []

def main():
    rowResponse = list(input("\n"+"Enter first row of first matrix: "))
    global firstMatrix
    global secondMatrix
    firstMatrix = []
    secondMatrix = []
    m1 = True
    m2 = False
    while m1:
        firstMatrix.append(rowResponse)
        rowResponse = input("Enter next row of matrix: ")
        if len(firstMatrix[0]) == len(rowResponse):
            rowResponse = list(rowResponse)
        else:
            m1 = False
            print("First Matrix" ,firstMatrix)
            rowResponse = list(input("Enter first row of second matrix: "))
            m2 = True
    while m2:
        secondMatrix.append(rowResponse)
        rowResponse = input("Enter next row of matrix: ")
        if len(secondMatrix[0]) == len(rowResponse):
            rowResponse = list(rowResponse)
        else:
            m2 = False
            print("Second Matrix: ", secondMatrix)
            choice()
            return firstMatrix, secondMatrix

def choice():
    userchoice = raw_input("What would you like to do with these two matrices? (add, subtract, multiply, or all): ")
    if userchoice == "add":
        if len(firstMatrix[0]) == len(secondMatrix[0]) and len(firstMatrix) == len(secondMatrix):
            print("The sum of the two matrices is {}".format(addMatrix(firstMatrix, secondMatrix, len(firstMatrix), len(firstMatrix[0]))))
        else:
            print("I'm sorry, we weren't able to subtract these two matrices. It seems that the first and second matrices possess different dimensions. Please try again and enter two valid ones.")
            main()
    elif userchoice == "subtract" or userchoice == "sub":
        if len(firstMatrix[0]) == len(secondMatrix[0]) and len(firstMatrix) == len(secondMatrix):
            print("The difference of the two matrices is {}".format(subtractMatrix(firstMatrix, secondMatrix, len(firstMatrix), len(firstMatrix[0]))))
        else:
            print("I'm sorry, we weren't able to subtract these two matrices. It seems that the first and second matrices possess different dimensions. Please try again and enter two valid ones.")
            main()
    elif userchoice == 'multiply':
        if len(firstMatrix[0]) == len(secondMatrix):
            print("The product of the two matrices is {}".format(multiplyMatrix(firstMatrix, secondMatrix, len(firstMatrix), len(firstMatrix[0]), len(secondMatrix[0]))))
        else:
            print("I'm sorry, we weren't able to multiply these two matrices. It seems that the first matrix posses a different number of columns than the second matrix's rows. Please try again and enter two valid ones")
            main()
    elif userchoice == "all":
        if len(firstMatrix[0]) == len(secondMatrix[0]) and len(firstMatrix) == len(secondMatrix):
            print("The sum of the two matrices is {}".format(addMatrix(firstMatrix, secondMatrix, len(firstMatrix), len(firstMatrix[0]))))
            print("\n" + "The difference of the two matrices is {}".format(subtractMatrix(firstMatrix, secondMatrix, len(firstMatrix), len(firstMatrix[0]))))
            print("\n" + "The product of the two matrices is {}".format(multiplyMatrix(firstMatrix, secondMatrix, len(firstMatrix), len(firstMatrix[0]), len(secondMatrix[0]))))
        else:
            print("I'm sorry, we weren't able to add, subtract, or multiply these two matrices. It seems the dimensions of these two matrices are incompatible. Please try again and enter two valid ones.")
            main()
    else:
        print(userchoice)
        print(type(userchoice))



def addMatrix(m1, m2, rowLength, columnLength):
    matrix3 = []
    x = 0
    while x < rowLength:
        templist = []
        y = 0
        while y < columnLength:
            templist.append(m1[x][y] + m2[x][y])
            y += 1
        x +=1
        matrix3.append(templist)
    return matrix3

def subtractMatrix(m1, m2, rowLength, columnLength):
    matrix3 = []
    x = 0
    while x < rowLength:
        templist = []
        y = 0
        while y < columnLength:
            templist.append(m1[x][y] - m2[x][y])
            y += 1
        x +=1
        matrix3.append(templist)
    return matrix3

def multiplyMatrix(m1, m2, rowLength, column, columnLength):
    matrix3 = []
    x = 0
    templist = []
    while x < rowLength:
        y2 = 0
        y = 0
        while y2 < columnLength:
            product = []
            y = 0
            while y < column:
                    product.append(m1[x][y] * m2[y][y2])
                    y += 1
            templist.append(product)
            y2+= 1
        x +=1
    z = 0
    for x in range(0, rowLength):
        tuple = []
        y = 0
        while y < columnLength:
            tuple.append(sum(templist[z]))
            y += 1
            z += 1
        matrix3.append(tuple)
    return matrix3



introduction()
