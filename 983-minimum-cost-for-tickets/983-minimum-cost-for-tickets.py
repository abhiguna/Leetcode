class Solution:
    # Approach: DP
    
    # Time = O(N^2)
    # Space = O(N)
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        N = len(days)
        table = [0 for _ in range(N)]
        # Base case
        table[0] = min(costs)
        
        for i in range(1, N):
            # Three cases
            # 1: buy a one day pass
            one_day = table[i-1] + costs[0]
            
            # 2: buy a two day pass
            j = i - 1
            while j >= 0 and days[j] >= days[i] - 6:
                j -= 1
            # There is valid day with a difference greater than 7 days
            if j >= 0:
                seven_day = table[j] + costs[1]
            # The difference between the first day and the current day is less than 7 days
            # So, just purchasing the 7-day pass should do.
            else:
                seven_day = costs[1]
            
            # 3: buy a thirty day pass
            j = i - 1
            while j >= 0 and days[j] >= days[i] - 29:
                j -= 1
            # There is valid day with a difference greater than 30 days
            if j >= 0:
                thirty_day = table[j] + costs[2]
            # The difference between the first day and the current day is less than 7
            # So, just purchasing the 7-day pass should do.
            else:
                thirty_day = costs[2]
            
            table[i] = min(one_day, seven_day, thirty_day)
        
        return table[N-1]
                