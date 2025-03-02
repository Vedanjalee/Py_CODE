def commonCharsInMultipleStrings(words):
    result =[]

    first_word = words[0]

    for char in first_word:
        found_in_all = True 

        for i in range(1, len(words)):
            if char in words[i]:
                words[i] = words[i].replace(char, '', 1)
            else:
                found_in_all = False 
                break 


        if found_in_all :
            result.append   (char)
    return result 

words1 = ["bella", "label", "roller"]
print(commonCharsInMultipleStrings(words1))      

words2 = ["cool", "lock", "cook"]
print(commonCharsInMultipleStrings(words2))      
