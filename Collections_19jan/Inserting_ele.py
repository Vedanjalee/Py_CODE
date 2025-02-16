from collections import deque 

de = deque([1,2,3])

de.append(4)

print(" deque after appenind : ")
print(de)

# Using appendleft() to insert ele at right end

de.appendleft(6)

print("deque after appending at left is : ")
print(de)