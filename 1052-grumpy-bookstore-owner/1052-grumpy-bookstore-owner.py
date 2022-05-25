class Solution:
    # Time = O(N)
    # Space = O(1)
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        N = len(customers)
        # Initialize
        # Compute the num satisifed -> when owner not grumpy
        num_satisfied = 0
        for i in range(N):
            if grumpy[i] == 0:
                num_satisfied += customers[i]
            
        num_angry = 0
        for i in range(minutes):
            if grumpy[i] == 1:
                num_angry += customers[i]
        
        global_max = num_angry + num_satisfied
        
        # General case, compute num_angry at each step and update global_max
        for i in range(minutes, N):
            if grumpy[i] == 1:
                num_angry += customers[i]
            if grumpy[i-minutes] == 1:
                num_angry -= customers[i-minutes]
            
            global_max = max(global_max, num_angry + num_satisfied)
        
        return global_max