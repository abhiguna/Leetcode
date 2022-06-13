class Solution:
    # Time = O(m+n), m: len(connections), n: # of nodes in the graph
    # Space = O(m+n)
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        adj_list = [[] for v in range(n)]
        arrival = [-1] * n
        departure = [-1] * n
        timestamp = [0]
        lowest_arrival = [-1] * n
        parent = [-1] * n
        visited = [-1] * n
        
        def build_graph():
            for (src, dest) in connections:
                adj_list[src].append(dest)
                adj_list[dest].append(src)
        
        build_graph()
        
        res = [] # Stores the bridges
        
        def dfs(node):
            arrival[node] = timestamp[0]
            timestamp[0] += 1
            visited[node] = 1
            lowest_arrival[node] = arrival[node]
            
            for nei in adj_list[node]:
                if visited[nei] == -1:
                    # Get the lowest arrival time for a neighbor
                    parent[nei] = node
                    lowest_arr_nei = dfs(nei)
                    # Update lowest arrival for the current node
                    lowest_arrival[node] = min(lowest_arrival[node], lowest_arr_nei)
                # We find if a backedge starts from the current node and update the
                #   lowest arrival time of the current node if possible
                elif nei != parent[node]:
                    lowest_arrival[node] = min(lowest_arrival[node], arrival[nei])
            
            # Check for a bridge and exclude the root
            if lowest_arrival[node] == arrival[node] and parent[node] != -1:
                res.append([parent[node], node])
            
            departure[node] = timestamp[0]
            timestamp[0] += 1
            # We have to return the earliest arrival time for which a backedge exists 
            # from the current node or its children
            return lowest_arrival[node]
            
            
        dfs(0) # Do a single dfs since the graph is connected
        return res