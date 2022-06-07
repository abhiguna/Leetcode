"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    # Time = O(M+N), M: # of edges in the graph, N: # of nodes in the graph
    # Space = O(N)
    def cloneGraph(self, node: 'Node') -> 'Node':
        # Edge case
        if not node:
            return None
        
        old_to_new = {}
        
        queue = deque()
        queue.append(node)
        old_to_new[node] = Node(node.val)
        
        while queue:
            src = queue.popleft()
            
            for nei in src.neighbors:
                if nei not in old_to_new:
                    old_to_new[nei] = Node(nei.val)
                    queue.append(nei)
                # Add two copies of each edge since connected, undirected graph
                old_to_new[src].neighbors.append(old_to_new[nei])
                    
        
        return old_to_new[node]
        