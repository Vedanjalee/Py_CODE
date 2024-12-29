arr = [2, 3, -8, 7, -1, 2, 3]

result = arr[0]
for i in range(len(arr)):
    currSum = 0

    for j in range(i, len(arr)):
        currSum = currSum + arr[j]

        result = max(result, currSum)
print(result)        