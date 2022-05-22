class Solution:
    # Time = O(Nlog(S-M)), N: len(weights), S: sum(weights), M: max(weights)
    # Space = O(1)
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # Edge case: days == 1
        if days == 1:
            return sum(weights)
        
        def num_days_to_ship(cap):
            days = 1
            load = 0
            for w in weights:
                load += w
                # If curr load greater than ship capacity, we need 1 more day to pack the curr item
                if load > cap:
                    days += 1
                    load = w
            return days
            
       # The weight of the ship must be at least the max weight in the set of items
       # Otherwise, we cannot pack that item in any ship
        w_start = max(weights) 
        w_end = sum(weights)
        while w_start <= w_end:
            w_mid = w_start + (w_end - w_start) // 2
            D = num_days_to_ship(w_mid)
            if D > days:
                w_start = w_mid + 1
            else:
                w_end = w_mid - 1
        return w_start # w_start points to the least weight capacity of the ship
        