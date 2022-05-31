class Solution:
    # Time = O(m+n)
    # Space = O(1)
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j, write_idx = m-1, n-1, m+n-1
        
        while i >= 0 and j >= 0:
            if nums2[j] > nums1[i]:
                nums1[write_idx] = nums2[j]
                j -= 1
            else:
                nums1[write_idx] = nums1[i]
                i -= 1
            write_idx -= 1
            
        while j >= 0:
            nums1[write_idx] = nums2[j]
            j -= 1
            write_idx -= 1
            
        return