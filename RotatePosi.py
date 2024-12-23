arr = [1, 2, 3, 4, 5]
k = 2
k = k% len(arr)
print(arr[-k: ] + arr[: -k])
