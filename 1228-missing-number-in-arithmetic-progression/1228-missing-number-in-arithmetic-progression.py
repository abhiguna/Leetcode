class Solution:
    # Time = O(logN)
    # Space = O(1)
    def missingNumber(self, arr: List[int]) -> int:
        # Arithmetic progression: a, a+d, a+2d, a+3d, ...., a+(n-1)d for n numbers
        N = len(arr)
        a = arr[0]
        # Here, to get d, we divide by N because we make N hops including the removed element.
        #.  Hence, the N-1th element will have a value of a+n*d instead of a + (n-1)*d
        d = (arr[N-1] - arr[0]) // N 
        
        # Edge case: if d == 0, all the values will be the same, so we return either the first or last element
        if d == 0:
            return arr[0]
        
        # Standard binary search algorithm
        start = 0
        end = N - 1
        # Two boundary zones: smaller zone | larger zone
        while start <= end:
            mid = start + (end - start) // 2
            if arr[mid] == a + (mid)*d:
                start = mid + 1
            else:
                end = mid - 1
        
        return arr[end] + d