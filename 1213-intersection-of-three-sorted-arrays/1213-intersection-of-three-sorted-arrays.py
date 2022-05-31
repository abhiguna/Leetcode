class Solution:
    # Time = O(M + N + K), M: len(arr1), N: len(arr2), K: len(arr3)
    # Space = O(1)
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        
        def intersect_two(nums1, nums2):
            res = []
            i, j = 0, 0
            while i < len(nums1) and j < len(nums2):
                if nums1[i] == nums2[j]:
                    res.append(nums1[i])
                    i += 1
                    j += 1
                elif nums1[i] < nums2[j]:
                    i += 1
                else:
                    j += 1
            return res
            
        intersection = intersect_two(arr1, arr2)
        res = intersect_two(intersection, arr3)
        return res