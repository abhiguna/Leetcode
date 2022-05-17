# Doubly Linked List Node
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
        
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        # LRU elements will be at the head -> we will remove from the head
        self.LRU = None
        # MRU elements will be at the tail -> we will append at the tail
        self.MRU = None
        self.hmap = {}
        
    def evict_and_append(self, node):
        del self.hmap[self.LRU.key]
        if self.LRU == self.MRU:
            self.LRU = self.MRU = node
            return
        # Evicting the least recently used element and appending the new element to the MRU side
        self.LRU = self.LRU.next
        self.LRU.prev = None
        node.prev = self.MRU
        self.MRU.next = node
        self.MRU = self.MRU.next
        return
    
    def extract_and_append(self, node):
        node_cpy = Node(node.key, node.value)
        # Append to the MRU side
        self.MRU.next = node_cpy
        node_cpy.prev = self.MRU
        self.MRU = self.MRU.next
        # Update hmap value for the current node
        self.hmap[node.key] = self.MRU
        if node == self.LRU:
            self.LRU = self.LRU.next
            self.LRU.prev = None
        else:
            # node has a prev ptr
            if node.prev:
                node.prev.next = node.next
            if node.next:
                node.next.prev = node.prev 
        return
            
        
    def get(self, key: int) -> int:
        # Key not found in hmap
        if key not in self.hmap:
            return -1
        # Key found in hashmap
        node = self.hmap[key]
        val = node.value 
        # Extract this node and add it to the tail
        self.extract_and_append(node)
        return val

    def put(self, key: int, value: int) -> None:
        # If element already there
        if key in self.hmap:
            node = self.hmap[key]
            node.value = value
            # Append to MRU side
            self.extract_and_append(node)
        else:
            new_node = Node(key, value)
            # Check if cache full -> LRU eviction needed
            if self.size == self.capacity:
                self.evict_and_append(new_node)
            else:
                self.size += 1
                
                if not self.LRU:
                    self.LRU = self.MRU = new_node
                else:
                    new_node.prev = self.MRU
                    self.MRU.next = new_node
                    self.MRU = self.MRU.next
            self.hmap[new_node.key] = new_node
        return


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)