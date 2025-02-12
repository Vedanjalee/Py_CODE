def myAtoi(s: str) -> int:
    
    i = 0
    n = len(s)
    sign = 1
    result = 0
    INT_MAX = 2**31 - 1 
    INT_MIN = -2**31     

    
    while i < n and s[i] == ' ':
        i += 1

    if i < n and s[i] in ['-', '+']:
        sign = -1 if s[i] == '-' else 1
        i += 1

    
    while i < n and s[i].isdigit():
        digit = int(s[i])
        result = result * 10 + digit

        
        if result >= (INT_MAX + 1) if sign == -1 else result > INT_MAX:
            return INT_MIN if sign == -1 else INT_MAX

        i += 1

    
    return sign * result




examples = ["42", "   -042", "1337c0d3", "0-1"]

for s in examples:
    print("Input:", '"' + s + '"', "Output:", myAtoi(s))
