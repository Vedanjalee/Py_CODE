arr = [12, 10, 9, 45, 2, 10, 10, 45]
#    Output: {12, 10, 9, 45, 2}
unique = []
for a in arr:
    if a not in unique:
        unique.append(a)
print(unique)        
