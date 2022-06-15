class Solution:
    # Time = O(m*nlog(m*n)) => O(n^2log(n)) for sparse graphs
    # Space = O(m+n) => size of the min heap
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # Implicit representation of edges
        m, n = len(heights), len(heights[0])
        captured = {} # captured[(r, c)] denotes the max effort required to reach (r, c) from (0, 0) in the grid
        
        def get_neighbors(i, j):
            neighbors = []
            if i+1 < m:
                neighbors.append((i+1, j))
            if j+1 < n:
                neighbors.append((i, j+1))
            if i-1 >= 0:
                neighbors.append((i-1, j))
            if j-1 >= 0:
                neighbors.append((i, j-1))
            return neighbors
        
        min_heap = []
        heappush(min_heap, (0, (0, 0)))
        
        while min_heap:
            (effort, (r, c)) = heappop(min_heap)
            
            if (r, c) in captured:
                continue
            
            captured[(r, c)] = effort
            for (nr, nc) in get_neighbors(r, c):
                if (nr, nc) not in captured:
                    max_effort = max(effort, abs(heights[nr][nc] - heights[r][c]))
                    heappush(min_heap, (max_effort, (nr, nc)))
        
        return captured[(m-1, n-1)]
            