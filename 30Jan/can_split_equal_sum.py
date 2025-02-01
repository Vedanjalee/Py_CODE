def can_split_equal_sum(a):
    total = sum(a)
    if total % 2 != 0:
        return False
    
    target = total // 2
    current_sum = 0
    
    for num in a:
        current_sum += num
        if current_sum == target:
            return True
    return False

a = [1, 2, 3, 6]
print(can_split_equal_sum(a))
