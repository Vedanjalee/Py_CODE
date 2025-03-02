def String_Merging(s1,s2, target):
    return target == (s1 + s2) or target==(s2+s1)

s1 = "hello"
s2 = "world"
target = "helloworld"

print("Can Merge:", String_Merging(s1, s2, target))