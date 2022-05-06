class Solution:
    # Time = O(M), M: total num chars in words list
    # Space = O(M)
    def alienOrder(self, words: List[str]) -> str:
        adj_list = {c: set() for w in words for c in w}
        def build_graph():
            for i in range(len(words) - 1):
                w1 = words[i]
                w2 = words[i+1]
                min_len = min(len(w1), len(w2))
                # Check invalid ordering -> same prefix but w2 has smaller len than w1
                if w1[:min_len] == w2[:min_len] and len(w2) < len(w1):
                    return True
                for j in range(min_len):
                    # Found the first differing character
                    if w1[j] != w2[j]:
                        adj_list[w1[j]].add(w2[j])
                        break
            return False
        
        is_invalid = build_graph()
        if is_invalid: return ""
        
        # --- Use DFS with visited hashmap to track backEdges
        alien_order = []
        visited = {}
        def dfs(src):
            if src in visited:
                return visited[src]
            visited[src] = True
            for nei in adj_list[src]:
                has_cycle = dfs(nei)
                if has_cycle: return True
            visited[src] = False
            alien_order.append(src)
        
        for c in adj_list:
            has_cycle = dfs(c)
            if has_cycle: return ""
        alien_order.reverse()
        return "".join(alien_order)
            