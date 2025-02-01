def pallindromicSubString(string, n):

    def count_pali_around_cnter(left, right):
        count = 0 
        while left>= 0 and right <n and string[left] == string[right]:
            count += 1
            left -= 1
            right += 1 
        return count 

    total_pallindromes = 0 

    for i in range(n):
        total_pallindromes += count_pali_around_cnter(i,i)

        total_pallindromes += count_pali_around_cnter(i,i+1)
   
    return total_pallindromes    


string = "abba"
n = len(string) 
result = pallindromicSubString(string, n)
print(string , " provided totalpallindromic substring count :    ", result)


