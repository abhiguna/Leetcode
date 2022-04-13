import math
import random

class Solution:
    def get_distance(self, point):
        return math.sqrt((point[0] ** 2) + (point[1] ** 2))
        
    def partition(self, points, start, end):
        pivot_idx = random.randint(start, end)
        # Swap
        points[start], points[pivot_idx] = points[pivot_idx], points[start]
        smaller = start
        for bigger in range(start + 1, end + 1):
            if self.get_distance(points[bigger]) <= self.get_distance(points[start]):
                smaller += 1
                # Swap
                points[smaller], points[bigger] = points[bigger], points[smaller]
        # Swap with pivot_idx
        points[start], points[smaller] = points[smaller], points[start]
        return smaller
        
    def helper(self, points, start, end, target_idx):
        # Base case
        if start == end:
            return
        
        pivot_idx = self.partition(points, start, end)
        if pivot_idx == target_idx:
            return
        elif pivot_idx < target_idx:
            self.helper(points, pivot_idx + 1, end, target_idx)
        else:
            self.helper(points, start, pivot_idx - 1, target_idx)
    
    # Time = O(N)
    # Space = O(1)
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        N = len(points)
        # Edge case
        if N == 1:
            return points
        
        self.helper(points, 0, N - 1, k - 1)
        return points[:k]
        
        