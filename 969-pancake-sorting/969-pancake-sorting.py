class Solution:
    # Time = O(N^2)
    # Space = O(1)
    def pancakeSort(self, arr: List[int]) -> List[int]:
        N = len(arr)
        res = []
        # D&C approch: Ensure that pancake i+1 appears in position i
        for i in range(N-1,-1,-1):
            if arr[i] != i+1:
                # Find the idx of the i+1th pancake to flip it two times
                for j in range(i, -1, -1):
                    if arr[j] == i+1:
                        break
                # Flip at j twice
                arr[:j+1] = arr[:j+1][::-1]
                arr[:i+1] = arr[:i+1][::-1]
                res.append(j+1)
                res.append(i+1)
        
        return res