from collections import *

class Solution:
    # Time = O(M+N)
    # Space = O(N)
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        M, N = len(nums1), len(nums2)
        stack = deque()
        hmap = {}
        for i in range(N-1, -1, -1):
            # Pop out all the elements that have a value <= current value
            while stack and stack[-1] <= nums2[i]:
                stack.pop()
            # If stack is not empty, we have a greater element to the right
            if stack:
                hmap[nums2[i]] = stack[-1]
            # If stack is EMPTY, we don't have any greater element to the right
            else:
                hmap[nums2[i]] = -1
            
            # Push the current element into the stack
            stack.append(nums2[i])
        
        res = []
        for i in range(M):
            res.append(hmap[nums1[i]])
        
        return res
                