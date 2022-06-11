class Solution:
    # Time = O(N)
    # Space = O(1)
    def findDuplicate(self, nums: List[int]) -> int:
        # Find meeting point
        hare, tortoise = 0, 0
        
        while True:
            hare = nums[nums[hare]]
            tortoise = nums[tortoise]
            if hare == tortoise:
                break
            
        # Find start of the cycle
        tortoise = 0
        while hare != tortoise:
            tortoise = nums[tortoise]
            hare = nums[hare]
        return tortoise