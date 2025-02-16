from collections import defaultdict 

def group_anagrams(words) :
    groups = defaultdict(list) 
    for word in words:
        sorted_word = ''.join(sorted(word)) 
        groups[sorted_word].append(word)
    return list(groups.values())

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = group_anagrams(words)
print(result)