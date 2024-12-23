arr = [1, 2, 3, 4, 5]
k = 9
prefix_sum ={}
curr_sum = 0
max_len = 0
# result=[]

for i in range(len(arr)):
    curr_sum += arr[i]
   
    if curr_sum == k:
        max_len = i+1
        # result =[(0,i)]
   
    if curr_sum - k  in prefix_sum:
        max_len = max(max_len, i-prefix_sum[curr_sum -k])

    if curr_sum not in prefix_sum: 
        prefix_sum [curr_sum] = i
print(max_len)       


