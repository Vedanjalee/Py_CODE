arr = [1, 5, 7, -1, 5]
target = 6
# print(find_pairs(arr, target))  # Output: [(5, 1), (5, 1)]
pairs = []
seen  = set()
for num in arr:

    complement = target - num

    if complement in seen: 
        pairs.append((num, complement))
    seen.add(num)
print(pairs)     