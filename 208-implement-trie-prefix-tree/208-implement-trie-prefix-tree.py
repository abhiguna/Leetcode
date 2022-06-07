# For inserting, searching, startingWith a string of length N
# Time = O(N)
# Space = O(N)
class Trie:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        

    def insert(self, word: str) -> None:
        curr = self
        for i in range(len(word)):
            if word[i] not in curr.children:
                curr.children[word[i]] = Trie()
            curr = curr.children[word[i]]
        
        # Set the last node to end of the word
        curr.is_end_of_word = True
        return
                
    def search(self, word: str) -> bool:
        curr = self
        for i in range(len(word)):
            if word[i] not in curr.children:
                return False
            curr = curr.children[word[i]]
        
        return curr.is_end_of_word
        

    def startsWith(self, prefix: str) -> bool:
        curr = self
        for i in range(len(prefix)):
            if prefix[i] not in curr.children:
                return False
            curr = curr.children[prefix[i]]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)