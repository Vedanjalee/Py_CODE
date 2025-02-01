
def longestValidParentheses( S) :
       
        stack, ans = [-1], 0

        
        for i in range(len(S)):
           
            if S[i] == '(':
                stack.append(i)
           
            else:
                if len(stack) == 1:
                    stack[0] = i
                else:
                    
                    stack.pop()
                   
                    ans = max(ans, i - stack[-1])

        return ans


example_input = "()())()"
print("Input:", example_input)
print("Longest Valid Parentheses Length:", longestValidParentheses(example_input))
