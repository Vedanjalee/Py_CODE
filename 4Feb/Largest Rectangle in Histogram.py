def largestRectangleArea(heights):
    max_area = 0 
    n = len(heights)

    for i in range(n) :
        left = i 
        while left >= 0  and heights[left] >= heights[i]: 
            left -= 1
        right =i
        
        while right < n and heights[right] >= heights[i]:
            right += 1  


        width = right - left - 1
        area = heights[i] * width
        max_area = max(max_area, area)
    
    return max_area    
print(largestRectangleArea([2,1,5,6,2,3]))  # Output: 10
