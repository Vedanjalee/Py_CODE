from collections import Counter 

def count_frequency(arr):
    freq = Counter(arr) 
    return freq  

arr =[1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
result = count_frequency(arr)
print(result)