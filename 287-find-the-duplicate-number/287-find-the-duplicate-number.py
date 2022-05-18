class Solution:
    # Time = O(N)
    # Space = O(1)
    def findDuplicate(self, nums: List[int]) -> int:
        # The duplicate element will create a cycle
        # We have to find the start of the cycle -> the idx where this occurs will be dup. ele.
        def f(idx):
            return nums[idx]
    
        hare, tortoise = 0, 0
        while True:
            hare = f(f(hare))
            tortoise = f(tortoise)
            # Cycle found
            if hare == tortoise:
                # Find the start of the cycle
                third = 0
                while third != tortoise:
                    tortoise = f(tortoise)
                    third = f(third)
                
                return third
        
        return -1