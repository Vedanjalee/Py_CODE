def smallest_common_element(mat):
    from collections import Counter

    row_count = len(mat)
    frequency = Counter()

   
    for num in mat[0]:
        frequency[num] += 1

    
mat = [
    [1, 2, 3, 4, 5],
    [2, 4, 5, 8, 10],
    [2, 5, 8, 9, 10]
]
print(smallest_common_element(mat)) 
