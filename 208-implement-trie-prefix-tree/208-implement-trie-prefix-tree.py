from collections import defaultdict 

class Trie:

    def __init__(self):
        self.word_map = set()
        self.prefix_map = defaultdict(list)

    def insert(self, word: str) -> None:
        if word in self.word_map:
            return None
        
        self.word_map.add(word)
        for i in range(1, len(word) + 1):
            self.prefix_map[word[:i]].append(word)
        
        return None
        
        

    def search(self, word: str) -> bool:
        return word in self.word_map
        

    def startsWith(self, prefix: str) -> bool:
        # print(self.prefix_map)
        word_list = self.prefix_map[prefix]
        return len(word_list) > 0
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)