def intersection_sorted_arrays(nums1, nums2):
    
    i, j = 0, 0  
    result = []  

    
    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:  
            result.append(nums1[i])
            i += 1
            j += 1
        elif nums1[i] < nums2[j]:  
            i += 1
        else:  
            j += 1

    return result


nums1 = [1, 2, 2, 3, 4, 5]
nums2 = [2, 2, 3, 6]

print("Array 1:", nums1)
print("Array 2:", nums2)

intersection = intersection_sorted_arrays(nums1, nums2)

print("Intersection:", intersection)
