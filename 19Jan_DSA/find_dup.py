from collections import Counter

def find_duplicates(arr):
    freq = Counter(arr)
    return [key for key, value in freq.items() if value > 1]


arr = [4, 3, 2, 7, 8, 2, 3, 1]
result = find_duplicates(arr)
print(result)  












