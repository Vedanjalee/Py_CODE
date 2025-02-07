
class Solution:
    def maxScore( nums1, nums2) :
        score1, score2 = 0, 0
       
        i, j = 0, 0
        
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                score1 += nums1[i]
                i += 1
            elif nums1[i] > nums2[j]:
                score2 += nums2[j]
                j += 1
            else:
                score1 = max(score1, score2) + nums1[i]
                score2 = score1
                i += 1
                j += 1
        
        while i < len(nums1):
            score1 += nums1[i]
            i += 1
        
        while j < len(nums2):
            score2 += nums2[j]
            j += 1
        
        return max(score1, score2)


solution = Solution()
print(solution.maxScore([1, 3, 5, 7], [2, 4, 6, 8]))  # Example Output: 30
from typing import List

class Solution:
    def maxScore( nums1, nums2) :
        score1, score2 = 0, 0
        
        i, j = 0, 0
        
       
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                score1 += nums1[i]
                i += 1
            elif nums1[i] > nums2[j]:
                score2 += nums2[j]
                j += 1
            else:
               
                score1 = max(score1, score2) + nums1[i]
                score2 = score1
                i += 1
                j += 1
        
       
        while i < len(nums1):
            score1 += nums1[i]
            i += 1
        
        while j < len(nums2):
            score2 += nums2[j]
            j += 1
        
      
        return max(score1, score2)


solution = Solution()
print(solution.maxScore([1, 3, 5, 7], [2, 4, 6, 8]))  # Output: 30
