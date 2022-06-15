class Solution:
    # Approach: finding the eulerian path ["Hierholzers Algorithm"]
    
    # Time = O(m+n), m: len(tickets), n: # of cities
    # Space = O(m+n)
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(reverse=True)
        adj_list = {}
        res = []
        
        def build_graph():
            for (src, dest) in tickets:
                if src not in adj_list:
                    adj_list[src] = []
                if dest not in adj_list:
                    adj_list[dest] = []
                    
                adj_list[src].append(dest)
        
        def dfs(node):
            while len(adj_list[node]) > 0:
                nei = adj_list[node].pop()
                dfs(nei)
            
            res.append(node)
                
        # Build the graph
        build_graph()
        
        # dfs populates the res in a reverse way
        dfs("JFK")
        res.reverse()
        return res
        