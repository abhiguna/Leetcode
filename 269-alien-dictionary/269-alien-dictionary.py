class Solution:
    # Time = O(n*m), n: len(words), m: avg. len of each word
    # Space = O(n*m)
    def alienOrder(self, words: List[str]) -> str:
        adj_list = {c: set() for word in words for c in word}
        in_deg = {c: 0 for word in words for c in word}
        
        # Build the graph
        for i in range(len(words) - 1):
            curr_word = words[i]
            nxt_word = words[i+1]
            # Edge case -> no valid topsort order
            min_len = min(len(curr_word), len(nxt_word))
            if curr_word[:min_len] == nxt_word[:min_len] and \
                len(curr_word) > len(nxt_word):
                return ""
            
            for j in range(min_len):
                if curr_word[j] != nxt_word[j]:
                    if nxt_word[j] not in adj_list[curr_word[j]]:
                        adj_list[curr_word[j]].add(nxt_word[j])
                        in_deg[nxt_word[j]] += 1
                    break
        
        # Kahn's topsort algorithm
        topsort = []
        queue = deque()
        for (key, val) in in_deg.items():
            if val == 0:
                topsort.append(key)
                queue.append(key)
                
        while queue:
            node = queue.popleft()
            
            for nei in adj_list[node]:
                in_deg[nei] -= 1
                if in_deg[nei] == 0:
                    topsort.append(nei)
                    queue.append(nei)
        
        # Check cycle
        if len(topsort) < len(in_deg):
            return ""
        
        return "".join(topsort)