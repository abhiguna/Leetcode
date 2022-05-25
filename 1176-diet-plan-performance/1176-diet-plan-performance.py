class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        # Initialization
        window_sum = sum(calories[:k])
        points = 0
        if window_sum < lower:
            points -= 1
        elif window_sum > upper:
            points += 1
        
        N = len(calories)
        for i in range(k, N):
            window_sum += (calories[i] - calories[i-k])
            if window_sum < lower:
                points -= 1
            elif window_sum > upper:
                points += 1
        
        return points