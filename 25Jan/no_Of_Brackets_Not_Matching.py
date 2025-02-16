def check_bracket_mismatch(str):
    if len(str) % 2 != 0 :
        return "Odd length can't have matching parenthesiis"
    
    stack = [] 
    matching_brackets = { 
        ')' : '(',
        '}' : '{' ,
        ']' : '['
    }

    for char in str : 
        if char in "({[" :
            stack.append(char)

        elif char in "]})" :
            if not stack or stack[-1] !=  matching_brackets[char]:
                return "Brackets are mismatched"
            stack.pop() 


    if stack : 
        return "Brackets are properly matched" 

    return "brackets are matched "

str = "{[]}()()((()))[{}][]{}"
print("Input:", str)
print("Check bracket mismatch ?..........:", check_bracket_mismatch(str))
