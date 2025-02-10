def get_subsets(arr, index, current):
    if index == len(arr):
        print(current)
        return

    
    get_subsets(arr, index + 1, current)

    get_subsets(arr, index + 1, current + [arr[index]])

arr = [1, 2, 3]
print("Subsets of the array:")
get_subsets(arr, 0, [])
