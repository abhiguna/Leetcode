class Solution:
    # Time = O(N)
    # Space = O(1)
    def circularArrayLoop(self, nums: List[int]) -> bool:
        N = len(nums)
        
        def f(idx):
            return (idx + nums[idx]) % N
        
        
        # Start the cycle-detection from each idx 
        for i in range(N):
            # Cycle starting at idx i is invalidated
            if nums[i] == 0:
                continue
                
            # Hare and tortoise store the idx position and not the value at that position
            hare, tortoise = i, i
            # Find the meeting point
            while True:
                hare = f(f(hare))
                tortoise = f(tortoise)
                if hare == tortoise:
                    # Find the length of the cycle
                    third = tortoise
                    positive = (nums[third] > 0) # tracks the current direction
                    count = 1
                    while f(third) != tortoise:
                        third = f(third)
                        # Check if direction is alternating
                        if (positive and nums[third] < 0) or \
                            (not positive and nums[third] > 0):
                            count = 1
                            break
                        count += 1
                    
                    # Check if cycle len == 1
                    if count == 1:
                        # Invalidate all the elements in the current cycle and then break
                        new_tortoise = i
                        while nums[new_tortoise] != 0:
                            next_loc = f(new_tortoise)
                            nums[new_tortoise] = 0
                            new_tortoise = next_loc
                        break
                    # Found a valid cycle
                    else:
                        return True
        return False