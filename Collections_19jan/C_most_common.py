from collections import Counter 

ctr = Counter([1,2,2,3,3,3,4,4,4,4,4])

common = ctr.most_common(3)

print(common)