class Solution:
    # Time = O(1) -> 4 digits generates 10^4 total combinations
    # Space = O(1)
    def openLock(self, deadends: List[str], target: str) -> int:
        dset = set(deadends)
        
        # Edge cases
        if target == "0000":
            return 0
        if "0000" in deadends: # If source in deadends -> can never reach target combination
            return -1
        
        visited = {"0000": 0}
        
        def get_neighbors(s):
            neighbors = []
            for i in range(len(s)):
                # Two possible comb. for each digit
                n1 = s[:i] + str((int(s[i])+1) % 10) + s[i+1:]
                n2 = s[:i] + str((int(s[i])-1) % 10) + s[i+1:]
                
                # Check if n1 or n2 is part of the set of deadends
                if n1 not in dset:
                    neighbors.append(n1)
                if n2 not in dset:
                    neighbors.append(n2)
            return neighbors
            
        def bfs(s):
            queue = deque()
            queue.append("0000")
            
            while queue:
                node = queue.popleft()
                
                for nei in get_neighbors(node):
                    if nei not in visited:
                        visited[nei] = 1 + visited[node]
                        queue.append(nei)
                        # Found target
                        if nei == target:
                            return visited[target]
            
            # Cannot reach target
            return -1
        
        
        return bfs("0000")