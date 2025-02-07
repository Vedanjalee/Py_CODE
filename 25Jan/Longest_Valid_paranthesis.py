
def longest_valid_parentheses(s):
     max_len =0 
     l = 0
     r = 0 
     

     for i in s:
          
          if i == '(' :
               l += 1
          elif i ==')' :
               r += 1

          if (l==r):
               max_len = max(max_len, l*2)
          elif (r>l):
               l =0 
               r =0 

     l =0 
     r =0

     for i in reversed(s):
          if i == ')'   :
               r += 1
          elif i == '(' :
               l+= 1 

          if l== r:
               max_len = max(max_len, l*2)
          elif (l>r):
               l =0 
               r =0                
     return max_len                         




print(longest_valid_parentheses("(()"))      # 2
print(longest_valid_parentheses(")()())"))  # 4

