class Solution:
    # Approach: 2-pointer approach
    
    # Time = O(N)
    # Space = O(1)
    def validMountainArray(self, arr: List[int]) -> bool:
        # Edge case: if len < 3
        if len(arr) < 3:
            return False
        
        N = len(arr)
        i = 0
        j = N - 1
        # Find peak from the left ptr
        for i in range(N-1):
            if arr[i] >= arr[i+1]:
                break
        
        # Find peak from the right ptr
        for j in range(N-1, 0, -1):
            if arr[j] >= arr[j-1]:
                break
        
        # Compare positions of the left and right ptr
        return (i == j)