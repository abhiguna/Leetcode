class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
    
class Trie:

    def __init__(self):
        self.root = TrieNode()
    
    # Time = O(N), N: len(word)
    # Space = O(N)
    def insert(self, word: str) -> None:
        curr = self.root
        
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        
        curr.is_end_of_word = True
        return
    
    # Time = O(N)
    # Space = O(1)
    def search(self, word: str) -> bool:
        curr = self.root
        
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        
        return curr.is_end_of_word

    # Time = O(M), M: len(prefix)
    # Space = O(1)
    def startsWith(self, prefix: str) -> bool:
        curr = self.root 
        
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)