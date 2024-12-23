arr = [40,50,30,401,21,50,30,30]
n = len(arr)

freq_map ={}
# for num in arr:
#     freq_map[num] = freq_map.get(num,0) + 1
# most_freq = max(freq_map, key= freq_map.get)   

for num in arr:
    if num in freq_map:
        freq_map[num] += 1
    else: 
        freq_map[num] = 1

most_freq = None
max_freq = 0

for num, freq in freq_map.items():
    if freq > max_freq :
        most_freq = num
        max_freq = freq
print(most_freq)        

