class Solution:
    # Time = O(m*n), m: avg length of each word, n: len(words)
    # Space = O(m*n)
    def alienOrder(self, words: List[str]) -> str:
        # Initialize adj_list and in_deg
        adj_list = {c: set() for word in words for c in word}
        in_deg = {c: 0 for c in adj_list.keys()}
        
        def build_graph():
            for i in range(len(words) - 1):
                word = words[i]
                next_word = words[i+1]
                
                # Edge case: same prefix but len(word) > len(word_2) 
                #     -> invalid lex. order
                min_len = min(len(word), len(next_word))
                if (word[:min_len]==next_word[:min_len]) and \
                    (len(word) > len(next_word)):
                    return False
                
                for j in range(min_len):
                    # Check if differs
                    if word[j] != next_word[j]:
                        # Edge case: skip duplicates
                        if next_word[j] not in adj_list[word[j]]:
                            adj_list[word[j]].add(next_word[j])
                            in_deg[next_word[j]] += 1
                        break
                
            return True
            
        # Build graph
        valid_input = build_graph()
        if not valid_input:
            return ""
        
        topsort = []
        
        # Topological sort
        queue = deque()
        for key, val in in_deg.items():
            if val == 0:
                queue.append(key)
        
        while queue:
            node = queue.popleft()
            topsort.append(node)
            
            for nei in adj_list[node]:
                in_deg[nei] -= 1
                if in_deg[nei] == 0:
                    queue.append(nei)
        
        # Check if cycle exists
        if len(topsort) < len(in_deg.keys()):
            return ""
        
        return "".join(topsort)
                    
                    