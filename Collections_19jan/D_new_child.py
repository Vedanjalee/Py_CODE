import collections 

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3 , 'c': 4}
dict3 = {'f' : 5}

chain = collections.ChainMap(dict1, dict2)

print(chain)

chain1 = chain.new_child(dict3)

print(chain1)