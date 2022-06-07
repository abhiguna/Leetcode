class Solution:
    # Time = O(N)
    # Space = O(1)
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def get_distance(point):
            return math.sqrt((point[0] ** 2) + (point[1] ** 2))
        
        def rand_quickselect(start, end):
            # Base case
            if start >= end:
                return
            
            pivot_idx = random.randint(start, end)
            (points[start], points[pivot_idx]) = (points[pivot_idx], points[start])
            pivot_dist = get_distance(points[start])
            
            # Lomuto's partitioning
            left = start
            for right in range(start+1, end+1):
                if get_distance(points[right]) <= pivot_dist:
                    left += 1
                    (points[left], points[right]) = (points[right], points[left])
            
            # Place pivot in its right pos
            (points[start], points[left]) = (points[left], points[start])
            
            if left == k:
                return
            elif left < k:
                return rand_quickselect(left+1, end)
            else:
                return rand_quickselect(start, left-1)
        
        
        N = len(points)
        rand_quickselect(0, N-1)
        return points[:k]