class Solution:
    # Time = O(N*2^N)
    # Space = O(N*2^N)
    def subsets(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        res = []
        # Enumerate all bitstrings of length N
        # 0 ... 2^N - 1
        for s in range(0, (1<<N)):
            p = N - 1
            slate = deque()
            while s != 0:
                # Rightmost bit is set
                if s & 1 == 1:
                    slate.appendleft(nums[p])
                p -= 1
                s = s >> 1
            res.append(slate)
        
        return res
                    