class Solution:
    # Time = O(N)
    # Space = O(1)
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # Cannot start from any gas station to reach it again
        if sum(cost) > sum(gas):
            return -1
        
        total = 0
        start_idx = 0
        for i in range(len(gas)):
            total += (gas[i] - cost[i])
            # If total diff becomes negative, set the next gas station to be the start idx
            if total < 0:
                start_idx = i + 1
                total = 0
        
        return start_idx
        
        