def partition(s):
    def is_palindrome(substring):
        return substring == substring[::-1]

    def backtrack(start_index, current_partition):
        if start_index == len(s):  
            all_partitions.append(current_partition[:]) 
            return
        
        for end_index in range(start_index + 1, len(s) + 1):
            substring = s[start_index:end_index]
            if is_palindrome(substring):
                current_partition.append(substring)  
                backtrack(end_index, current_partition) 
                current_partition.pop()  
    
    all_partitions = []
    backtrack(0, [])
    return all_partitions
print(partition("aab"))
