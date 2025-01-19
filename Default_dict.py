from collections import defaultdict 

d = defaultdict(int)

L = [1, 2, 3, 4, 2, 4, 1, 2] 

for i in L:

    d[i] += 1
print(d)    