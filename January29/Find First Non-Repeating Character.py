from  collections import Counter 

def first_non_repeating_char(s):

    char_count = Counter(s)

    for index, char in enumerate(s):
        if char_count[char] == 1:
            print("non repating char ", char,"at index", index)
            
        else:
            print("Non repeating char found")
            
s = "swiss"
result = first_non_repeating_char(s)
print(result)
