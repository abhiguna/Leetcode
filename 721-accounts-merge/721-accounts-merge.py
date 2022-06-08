class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_to_name = defaultdict(str)
        adj_list = defaultdict(set)
        visited = set()
        res = []
        
        def build_graph():
            for acc in accounts:
                for e in range(1, len(acc)):
                    email_to_name[acc[e]] = acc[0]
                    
                
                for i in range(2, len(acc)):
                    adj_list[acc[1]].add(acc[i])
                    adj_list[acc[i]].add(acc[1])

            return
                
                
        
        def bfs(email):
            queue = deque()
            queue.append(email)
            visited.add(email)
            min_heap = []
            heappush(min_heap, email)
            
            while queue:
                curr_email = queue.popleft()
                
                for nemail in adj_list[curr_email]:
                    if nemail not in visited:
                        visited.add(nemail)
                        heappush(min_heap, nemail)
                        queue.append(nemail)
            
            account = []
            account.append(email_to_name[min_heap[0]])
            while len(min_heap) > 0:
                account.append(heappop(min_heap))
            res.append(account)
            return
            
            
        
        build_graph()
        for email in email_to_name.keys():
            if email not in visited:
                bfs(email)
        
        return res
    
        