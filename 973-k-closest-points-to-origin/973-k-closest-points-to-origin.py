from collections import defaultdict
import heapq

class Solution:
    # Time = O(n + klogn)
    # Space = O(n)
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def calcDist(point):
            return math.sqrt(point[0]**2 + point[1]**2)
        
        point_dist = []
        lookup = defaultdict(list)
        for point in points:
            dist_from_or = calcDist(point)
            point_dist.append(dist_from_or)
            lookup[dist_from_or].append(point)
        k_closest = []
        heapq.heapify(point_dist)
        i = 0
        while i < k:
            min_dist = heapq.heappop(point_dist)
            points = lookup[min_dist]
            for point in points:
                if i == k:
                    break
                k_closest.append(point)
                i += 1
        return k_closest