def wordBreak(s: str, wordDict: list) -> bool:
    word_set = set(wordDict)  
    n = len(s)
    
    dp = [False] * (n + 1)
    dp[0] = True 


    for i in range(1, n + 1):
        for j in range(i):
            
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break  

    return dp[n]


s = "leetcode"
wordDict = ["leet", "code"]
print(wordBreak(s, wordDict)) 



s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
print(wordBreak(s, wordDict))  