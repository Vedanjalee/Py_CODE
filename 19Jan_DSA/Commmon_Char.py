from collections import Counter 

def common_chars(words):
    common = Counter(words[0]) 
    for word in words[1:] :
        common &= Counter(word) 
    return list(common.elements())

words = ["bella", "label", "roller"]
result = common_chars(words)
print(result)