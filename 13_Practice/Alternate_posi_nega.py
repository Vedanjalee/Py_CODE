def posi_nega(nums):
    posi =[]
    nega =[]

    for num in nums:
        if num>= 0:
            posi.append(num)
        else:
            nega.append(num)

    result = []
    i,j=0,0 

    while i<len(posi) and j<len(nega):
        result.append(posi[i])
        result.append(nega[i])

        i+= 1
        j+= 1

    while i<len(posi):
        result.append(posi[i])
        i += 1
    while j<len(nega):
        result.append(nega[j])
        j += 1
    return result 

nums = [1,2,3,-4,-1,4]
print(posi_nega(nums))            
