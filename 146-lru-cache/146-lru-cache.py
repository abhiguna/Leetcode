class CacheNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
        
class LRUCache:
    def __init__(self, capacity: int):
        self.LRU = None
        self.MRU = None
        self.hmap = {}
        self.capacity = capacity
        self.size = 0

    def extract_and_append(self, node):
        node_cpy = CacheNode(node.key, node.val)
        self.hmap[node.key] = node_cpy
        # Add to the end
        self.MRU.next = node_cpy
        node_cpy.prev = self.MRU
        self.MRU = self.MRU.next 
        
        if self.LRU == node:
            self.LRU = self.LRU.next 
            self.LRU.prev = None
        else:
            if node.prev:
                node.prev.next = node.next 
            if node.next:
                node.next.prev = node.prev 
        return
    
    def evict_and_append(self, node):
        del self.hmap[self.LRU.key]
        # Append the node
        # Edge case: singleton LRUCache
        if self.LRU == self.MRU:
            self.LRU = self.MRU = node
        else:
            self.MRU.next = node
            node.prev = self.MRU 
            self.MRU = self.MRU.next 
            self.LRU = self.LRU.next 
            self.LRU.prev = None
        return
    
    def get(self, key: int) -> int:
        if key not in self.hmap:
            return -1
        else:
            node = self.hmap[key]
            self.extract_and_append(node)
            return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.hmap:
            node = self.hmap[key]
            node.val = value
            self.extract_and_append(node)
        else:
            node = CacheNode(key, value)
            self.hmap[key] = node
            if self.size == self.capacity:
                self.evict_and_append(node)
            else:
                self.size += 1
                if not self.LRU:
                    self.LRU = self.MRU = node
                else:
                    self.MRU.next = node
                    node.prev = self.MRU
                    self.MRU = self.MRU.next
        return


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)