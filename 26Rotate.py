nums1 = [1, 2, 3, 4, 5, 6, 7]
k = 3
# print(rotate(nums1, k1))  # Output: [5, 6, 7, 1, 2, 3, 4]

# n = len(nums1)

k = k+1%len(nums1)



ret =[]

ret = nums1[k:] + nums1[:k]
print(ret) 
    
