def score_of_paranthesis(s):

    stack =[]
    score = 0

    for char in s:
        if char == '(':
            stack.append(score)
            score =0

        else:
            
            last_score = stack.pop() 

            score = last_score + max(2* score, 1)

    return score

# Test Cases
print(score_of_paranthesis("()"))        # Output: 1
print(score_of_paranthesis("(())"))      # Output: 2
print(score_of_paranthesis("()()"))      # Output: 2
print(score_of_paranthesis("(()(()))"))  # Output: 6