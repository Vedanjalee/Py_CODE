from collections import Counter 
c = Counter(['a', 'b', 'c', 'a', 'b' , 'a']) 

print(c)

print(c['a'])

print(c.most_common(1))