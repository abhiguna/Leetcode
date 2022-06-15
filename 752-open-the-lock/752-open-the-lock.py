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
        
        f_visited = {"0000": 0}
        b_visited = {target: 0}
        
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
            
        def bidir_bfs():
            f_queue = deque()
            f_queue.append("0000")
            
            b_queue = deque()
            b_queue.append(target)
            
            while f_queue and b_queue:
                f_node = f_queue.popleft()
                
                for f_nei in get_neighbors(f_node):
                    if f_nei not in f_visited:
                        f_visited[f_nei] = 1 + f_visited[f_node]
                        f_queue.append(f_nei)
                        # Found target
                        if f_nei in b_visited:
                            return f_visited[f_nei] + b_visited[f_nei]
                
                b_node = b_queue.popleft()
                
                for b_nei in get_neighbors(b_node):
                    if b_nei not in b_visited:
                        b_visited[b_nei] = 1 + b_visited[b_node]
                        b_queue.append(b_nei)
                        # Found target
                        if b_nei in f_visited:
                            return b_visited[b_nei] + f_visited[b_nei]
            
            # Cannot reach target
            return -1
        
        
        return bidir_bfs()