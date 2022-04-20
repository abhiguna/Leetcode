class Solution:
    # Time = O(M + N)
    # Space = O(1)
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        ptr1 = m - 1
        ptr2 = n - 1
        write = m + n - 1
        
        while ptr1 >= 0 and ptr2 >= 0:
            if nums1[ptr1] > nums2[ptr2]:
                nums1[write] = nums1[ptr1]
                ptr1 -= 1
            else:
                nums1[write] = nums2[ptr2]
                ptr2 -= 1
            
            write -= 1
        
        # ptr1 out of bounds
        while ptr2 >= 0:
            nums1[write] = nums2[ptr2]
            ptr2 -= 1
            write -= 1
        
        return
        