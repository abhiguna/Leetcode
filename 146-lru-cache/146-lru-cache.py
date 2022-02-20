from collections import defaultdict
from sortedcontainers import SortedDict

class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.max_size = capacity
        self.cache = defaultdict()
        self.lru, self.mru = Node(0, 0), Node(0, 0)
        self.lru.next, self.mru.prev = self.mru, self.lru
        
    # remove from lru
    def remove(self, node):
        prev_node, next_node = node.prev, node.next
        prev_node.next, next_node.prev = next_node, prev_node
    
    # insert at mru
    def insert(self, node):
        prev_node, next_node = self.mru.prev, self.mru
        prev_node.next = next_node.prev = node
        node.prev, node.next = prev_node, next_node
    
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        if len(self.cache) > self.max_size:
            lru = self.lru.next
            self.remove(lru)
            del self.cache[lru.key]
    


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)