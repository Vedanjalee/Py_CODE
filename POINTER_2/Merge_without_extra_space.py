def merge_without_extra_space(arr1, arr2):
    n, m = len(arr1), len(arr2)
    i, j = n - 1, 0  

    while i >= 0 and j < m:
        if arr1[i] > arr2[j]:
            arr1[i], arr2[j] = arr2[j], arr1[i]
        i -= 1
        j += 1

    arr1.sort()
    arr2.sort()


arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]

print("Before merging:")
print("arr1: ",arr1)
print("arr2: ",arr2)

merge_without_extra_space(arr1, arr2)

print("\nAfter merging:")
print("arr1: ",arr1)
print("arr2: ",arr2)