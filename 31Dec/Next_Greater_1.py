def nextGreaterElement(nums1, nums2) :
        next_greater = {}
        stack = []

        for num in nums2:
            while stack and num > stack[-1]:
                smaller = stack.pop()
                next_greater[smaller] = num
            stack.append(num)

        while stack:

            next_greater[stack.pop()] = -1

        return [next_greater[num] for num in nums1]

nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
print("Output:",nextGreaterElement(nums1, nums2))  

nums1 = [2, 4]
nums2 = [1, 2, 3, 4]
print("Output:", nextGreaterElement(nums1, nums2))    