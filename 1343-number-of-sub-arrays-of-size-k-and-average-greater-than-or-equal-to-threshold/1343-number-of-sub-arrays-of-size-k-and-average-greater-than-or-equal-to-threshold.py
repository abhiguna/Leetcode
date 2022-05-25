class Solution:
    # Time = O(N)
    # Space = O(1)
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # Initialization
        window_sum = sum(arr[:k])
        if window_sum >= threshold * k:
            count = 1
        else:
            count = 0
        
        N = len(arr)
        
        # General case
        for i in range(k, N):
            window_sum += (arr[i] - arr[i-k])
            if window_sum >= threshold * k:
                count += 1
        
        return count