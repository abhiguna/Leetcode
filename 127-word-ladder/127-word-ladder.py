class Solution:
    # Time = O(N*M^2)
    # Space = O(N*M^2)
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Edge case
        if endWord not in wordList:
            return 0
        
        adj_list = defaultdict(list)
        wordList.append(beginWord)
        
        def build_graph():
            for word in wordList:
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    adj_list[pattern].append(word)

        visited = set()
        
        def bfs():
            queue = deque()
            queue.append(beginWord)
            visited.add(beginWord)
            words_in_path = 1
            
            while queue:
                num_nodes = len(queue)
                # Traverse layer by layer
                for i in range(num_nodes):
                    node = queue.popleft()
                    if node == endWord:
                        return words_in_path
                    for j in range(len(node)):
                        pattern = node[:j] + "*" + node[j+1:]
                        for nei in adj_list[pattern]:
                            if nei not in visited:
                                visited.add(nei)
                                queue.append(nei)
                
                words_in_path += 1
            return 0
        
        build_graph()
        return bfs()
        