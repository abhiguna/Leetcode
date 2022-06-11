class Node:
    def __init__(self, freq, word):
        self.freq = freq
        self.word = word
    
    # Custom comparator
    def __lt__(self, other):
        if self.freq == other.freq:
            return self.word > other.word
        return self.freq < other.freq
    
    
class Solution:
    # Time = O(Nlogk)
    # Space = O(N)
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_freq = Counter(words)
        
        min_heap = []
        for (word, freq) in word_freq.items():
            heappush(min_heap, Node(freq, word))
            
            if len(min_heap) > k:
                heappop(min_heap)
        
        return [heapq.heappop(min_heap).word for _ in range(k)][::-1]
        