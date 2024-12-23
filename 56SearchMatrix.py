def searchMatrix(mat, x):
    """
    Search for a number in a row-column sorted matrix.

    Args:
    mat: List of lists of integers, the matrix to search.
    x: Integer, the target value to search for.

    Returns:
    bool: True if x is found in the matrix, otherwise False.
    """
    # Number of rows
    n = len(mat)
    # Number of columns
    m = len(mat[0])
    
    # Start from the top-right corner of the matrix
    row = 0
    col = m - 1
    
    # Traverse the matrix
    while row < n and col >= 0:
        # If the current element matches x
        if mat[row][col] == x:
            return True  # Found the element
        # If the current element is greater than x,
        # move left (reduce column index)
        elif mat[row][col] > x:
            col -= 1
        # If the current element is less than x,
        # move down (increase row index)
        else:
            row += 1
    
    # If we exit the loop, x is not in the matrix
    return False

# Example usage
mat1 = [[3, 30, 38], [20, 52, 54], [35, 60, 69]]
x1 = 62
print(searchMatrix(mat1, x1))  # Output: False

mat2 = [[18, 21, 27], [38, 55, 67]]
x2 = 55
print(searchMatrix(mat2, x2))  # Output: True

mat3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
x3 = 3
print(searchMatrix(mat3, x3))  # Output: True
