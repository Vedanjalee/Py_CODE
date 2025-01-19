from collections import OrderedDict

def first_non_repeat_char(s):

    counts = OrderedDict()

    for char in s :
        counts[char] = counts.get(char, 0) + 1 

    for char , count in counts.items() :
        if count == 1:
            return char 
        
    return None 

s = "swiss"
result = first_non_repeat_char(s)
print(result)


