from collections import deque 

de = deque([1,6,2,3,4])

de.pop() 

print("the deque after deleting from right is : ")
print(de)

de.popleft() 

print ("The deque after deleting from left is : ") 
print (de)