def row_wise_sum(matrix):
    row_index = 1  
    for row in matrix:  
        row_sum = sum(row)  
        print("Row " ,row_index , "sum" ,row_sum) 
        row_index += 1  


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Row-wise Sums:")
row_wise_sum(matrix)