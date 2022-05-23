class Solution:
    # Time = O(log(M + N))
    # Space = O(1)
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        M = len(nums1)
        N = len(nums2)
        
        # Odd number of elements
        if (M+N) % 2 == 1:
            k = (M+N)//2 + 1
        # Even number of elements
        else:
            k = (M+N)//2
        
        # Returns the value at a given idx
        # -math.inf if idx < 0, math.inf if idx >= M, otherwise A[idx]
        def get(A, idx):
            if idx < 0:
                return float("-inf")
            elif idx >= len(A):
                return float("inf")
            else:
                return A[idx]
        
        start = 0
        end = M - 1
        while start <= end:
            # We search for the kth element using the first list
            mid = start + (end - start) // 2
            # Mid value is the kth smallest element
            if get(nums2, k-1-mid-1) <= get(nums1, mid) <= get(nums2, k-1-mid):
                kth_smallest = get(nums1, mid)
                succ = min(get(nums1, mid+1), get(nums2, k-1-mid))
                break
            # Kth smallest in the left half
            elif get(nums1, mid) > get(nums2, k-1-mid):
                end = mid - 1
            # Kth smallest in the right half
            else:
                start = mid + 1
        
        # Kth smallest value not found
        if start == end + 1:
            kth_smallest = get(nums2, k-start-1)
            succ = min(get(nums1, start), get(nums2, k-start))
        
        # Return the appropriate median depending on whether the input has an even or odd number of elements
        if (M+N) % 2 == 1:
            return kth_smallest
        else:
            return (kth_smallest + succ) / 2.0
            
            
            
            