def isPalindrome(s: str) -> bool:
    return s == s[::-1]  

def palindromePartitioning(s) :
    result = []

    
    def backtrack(start, path):
       
        if start == len(s):
            result.append(path[:])
            return

        for end in range(start + 1, len(s) + 1):
            substring = s[start:end]
            
           
            if isPalindrome(substring):
                path.append(substring) 
                backtrack(end, path)   
                path.pop()            

    backtrack(0, [])
    return result


s = "aab"
print("Palindrome partitions:", palindromePartitioning(s))
