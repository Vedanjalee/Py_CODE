def searchMatrix(matrix, target):
    for row in matrix:
        for element in row:
            if element == target:
                return True
    return False


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
target = 5
print("Target found:", searchMatrix(matrix, target))  

target = 10
print("Target found:", searchMatrix(matrix, target))  
