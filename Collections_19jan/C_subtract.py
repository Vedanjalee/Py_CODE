from collections import Counter 

ctr = Counter([1,2,2,3,3,3])

ctr.subtract([2,3,3])

print(ctr)