class Solution:
    # Time = O(N)
    # Space = O(1)
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def get_distance(point):
            return math.sqrt((point[0]**2) + (point[1]**2))
        
        def helper(start, end):
            if start >= end:
                return 
            
            pivot_idx = random.randint(start, end)
            (points[start], points[pivot_idx]) = (points[pivot_idx], points[start])
            pivot = get_distance(points[start])
            # Lomuto's partitioning 
            left = start
            for right in range(start+1, end+1):
                if get_distance(points[right]) <= pivot:
                    left += 1
                    (points[left], points[right]) = (points[right], points[left])
            
            (points[start], points[left]) = (points[left], points[start])
            
            if left == k:
                return
            elif left < k:
                return helper(left + 1, end)
            else:
                return helper(start, left - 1)
            
            
        
        helper(0, len(points) - 1)
        return points[:k]