def findFirstOccurrence(arr, target):
    low, high = 0, len(arr) - 1
    result = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            result = mid
            high = mid - 1  # Keep searching on the left
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return result


def findLastOccurrence(arr, target):
    low, high = 0, len(arr) - 1
    result = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            result = mid
            low = mid + 1  # Keep searching on the right
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return result

arr =[1,2,3,3,3,4,5,6,]
target = 3
ans1 = findFirstOccurrence(arr, target)
ans2 = findLastOccurrence(arr, target)

print(ans1,ans2)

