def string_to_integer(s):

    result = 0
    is_negative = False 
    start_idx = 0 

    if s[0] == '-':
        is_negative = True 
        start_index = 0 

    for i in range(start_index , len(s)):

        if s[i].isdigit():

            result = result *10 + (ord(s[i] ) - ord('0'))
        else:
            print("invalid char")


    if is_negative : 
        result = -result 
    return result 

string_number = "-1234"
integer_value = string_to_integer(string_number)
print("Converted integer value : " ,integer_value)                 