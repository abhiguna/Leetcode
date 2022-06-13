class Solution:
    # Time = O(n*mlog(n*m)), n: len(accounts), m: avg. length of each account 
    # Space = O(n*m)
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        adj_list = defaultdict(set)
        email_to_name = {}
        
        def build_graph():
            for idx, acc in enumerate(accounts):
                email_to_name[acc[1]] = acc[0]
                
                for email in acc[2:]:
                    email_to_name[email] = acc[0]
                    adj_list[acc[1]].add(email)
                    adj_list[email].add(acc[1])
                
        
        build_graph()
        
        visited = set()
        res = []
        account = []
        
        def dfs(src):
            visited.add(src)
            account.append(src)
            
            for nei in adj_list[src]:
                if nei not in visited:
                    dfs(nei)
            
        
        for e in email_to_name:
            if e not in visited:
                dfs(e)
                account.sort()
                res.append([email_to_name[account[0]]] + [acc for acc in account])
                account = []
        
        return res
                
        
        
        
        

        