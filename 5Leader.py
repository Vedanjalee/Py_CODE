def find_leaders(arr):
    n = len(arr)  # Get the size of the array
    leaders = []  # List to store leaders
    max_from_right = arr[-1]  # Start with the last element as the initial leader
    leaders.append(max_from_right)

    # Traverse the array from second last to the first
    for i in range(n - 2, -1, -1):  # (start, stop, step)
        if arr[i] > max_from_right:
            max_from_right = arr[i]  # Update the maximum
            leaders.append(max_from_right)

    # Reverse the leaders list since we collected them in reverse order
    return leaders[::-1]


# Example usage
arr = [16, 17, 4, 3, 5, 2]
print("Leaders in the array:", find_leaders(arr))
