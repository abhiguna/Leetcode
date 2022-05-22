class Solution:
    # Time = O(NlogM), N: len(piles), M: max(piles)
    # Space = O(1)
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Edge case: if h == len(piles)
        if h == len(piles):
            return max(piles)
        
        # M = max bananas per pile
        M = max(piles)
        k_start = 1
        k_end = M
        while k_start <= k_end:
            k_mid = k_start + (k_end - k_start) // 2
            # Compute total hrs needed if speed of eating bananas is k_mid
            hrs_needed = 0
            for p in piles:
                hrs_needed += math.ceil(1.0 * (p/k_mid))
            
            # Boundary: hrs_needed > h | hrs_needed <= h
            if hrs_needed > h:
                k_start = k_mid + 1
            else:
                k_end = k_mid - 1
        # At the end, k_start points to the minimum speed of eating bananas
        return k_start