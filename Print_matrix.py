def printMatrix(matrix):
    
    for row in matrix: 
        for element in row:          
            print(element, end=" ")  
        print()  
        
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

print("Matrix Elements:")
print(printMatrix(matrix))