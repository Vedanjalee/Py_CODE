arr = [5, 3, 8, 6, 2]
order = [2, 5, 8, 3, 6]

sorted_arr =[]

for num in order:
    if num in arr:
        sorted_arr.append(num)
print(sorted_arr)    