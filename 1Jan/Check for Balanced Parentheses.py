def isValid(s) :
    st = []
    for paranthesis in s:
        if paranthesis == '(' or paranthesis == '{' or paranthesis == '[':
            st.append(paranthesis)
        else:
            if len(st) == 0:
                return False
            ch = st[-1]
            st.pop()
            if (paranthesis == ')' and ch == '(') or (paranthesis == ']' and ch == '[') or (paranthesis == '}' and ch == '{'):
                continue
            else:
                return False
    return len(st) == 0


s = "()[{}()]"
if isValid(s):
    print("True")
else:
    print("False")