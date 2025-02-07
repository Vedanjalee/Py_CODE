from collections import Counter

def top_k_frequent_element(arr, k):
    c = Counter(arr)
    # return(c.most_common(k))

    return [key for key, _ in c.most_common(k)]




arr = [1, 1, 1, 2, 2, 3, 3, 3, 3]
k = 2
result = top_k_frequent_element(arr, k)
print(result)