def longest_mountain(arr):
    n = len(arr)
    if n < 3:
        return 0

    longest = 0

    
    for i in range(1, n - 1):
       
        if arr[i - 1] < arr[i] > arr[i + 1]:
            
            left = i - 1
           
            while left > 0 and arr[left - 1] < arr[left]:
                left -= 1

            right = i + 1
            while right < n - 1 and arr[right] > arr[right + 1]:
                right += 1

            
            mountain_length = right - left + 1
            longest = max(longest, mountain_length)

    return longest



arr = [2, 1, 4, 7, 3, 2, 5]
print("Longest Mountain Length:", longest_mountain(arr))
