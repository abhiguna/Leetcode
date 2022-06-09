class Solution:
    # Time = O(N*M^2) N: len(wordList), M: len(wordList[0])
    # Space = O(N^2*M)
    
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Add beginWord to list
        wordList.append(beginWord)
        word_set = set(wordList)
        adj_list = defaultdict(set)
        visited = set()
        
        def build_graph():
            for i in range(len(wordList)):
                for j in range(0, len(wordList[i])):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        word = wordList[i]
                        t_word = word[:j] + c + word[j+1:]
                        if t_word in word_set:
                            adj_list[word].add(t_word)
            return
        
        # Finds the shortest path len
        path_len = [1]
        
        def bfs():
            queue = deque()
            queue.append(beginWord)
            visited.add(beginWord)
            
            while queue:
                num_nodes = len(queue)
                
                # Process nodes level-by-lvel
                for i in range(num_nodes):
                    node = queue.popleft()
                
                    if node == endWord:
                        return path_len[0]

                    for nei in adj_list[node]:
                        if nei not in visited:
                            visited.add(nei)
                            queue.append(nei)

                path_len[0] += 1
    
            return 0
        
        build_graph()
        return bfs()
        
        
        