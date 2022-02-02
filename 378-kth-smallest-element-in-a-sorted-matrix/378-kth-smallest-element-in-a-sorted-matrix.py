import heapq

class Solution:
    # Time: O(n^2 + nlogk)
    # Space: O(k)
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        max_heap = []
        heapq.heapify(max_heap)
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                heapq.heappush(max_heap, -1*matrix[i][j])
                if len(max_heap) > k:
                    heapq.heappop(max_heap)
        return -1*heapq.heappop(max_heap)