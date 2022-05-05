class Solution:
    # Time = O(N*M + N^2)
    # Space = O(N*M*M)
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList.append(beginWord)
        adj_list = defaultdict(list)
    
        def build_graph():
            for word in wordList:
                for idx in range(len(word)):
                    pattern = word[:idx] + "*" + word[idx+1:]
                    adj_list[pattern].append(word)
            return
        
        visited = set()

        def bfs():
            queue = deque([beginWord])
            visited.add(beginWord)
            slen = 1
            
            while queue:
                num_words = len(queue)
                
                for _ in range(num_words):
                    word = queue.popleft()
                    
                    if word == endWord:
                        return slen
                    
                    for idx in range(len(word)):
                        pattern = word[:idx] + "*" + word[idx+1:]
                        for nei in adj_list[pattern]:
                            if nei not in visited:
                                visited.add(nei)
                                queue.append(nei)
                slen += 1
            
            # No path exists
            return 0
            
        
        build_graph()
        return bfs()