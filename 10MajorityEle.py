nums = [2, 2, 1, 1, 1, 2, 2]

n = len(nums) 
count = 0
ele = None 

for i in range(n):
    if count == 0:
        ele = nums[i]
        count = 1
    elif nums[i] == ele:
        count += 1 
    else:
        count -= 1  

count1 = 0
for i in range(n):
    if nums[i] == ele:
        count1 += 1

if count1 > (n // 2):  
    print(ele)
else:
    print("No majority element found")
