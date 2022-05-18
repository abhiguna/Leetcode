class ListNode:
    def __init__(self, val=-1, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        
    def get(self, index: int) -> int:
        curr = self.head
        node_idx = 0
        while curr and node_idx != index:
            curr = curr.next 
            node_idx += 1
        return curr.val if curr else -1

    def addAtHead(self, val: int) -> None:
        node = ListNode(val)
        node.next = self.head
        self.head = node
        # Empty list
        if not self.tail:
            self.tail = node
        return

    def addAtTail(self, val: int) -> None:
        node = ListNode(val)
        # Empty list
        if not self.head:
            self.head = self.tail = node
            return
        self.tail.next = node
        self.tail = node
        return
        

    def addAtIndex(self, index: int, val: int) -> None:
        # Sentinel node
        sentinel = ListNode(-math.inf, self.head)
        
        prev, curr = sentinel, self.head
        node_idx = 0
        while curr and node_idx != index:
            prev = curr
            curr = curr.next
            node_idx += 1
        
        node = ListNode(val)
        if curr:
            prev.next = node
            node.next = curr
        # Update head and tail ptrs
        # Change tail only if you insert at the end
        elif node_idx == index:
            prev.next = node
            self.tail = node
                
        self.head = sentinel.next
        return
        

    def deleteAtIndex(self, index: int) -> None:
        # Sentinel node
        sentinel = ListNode(-math.inf, self.head)
        
        prev, curr = sentinel, self.head
        node_idx = 0
        while curr and node_idx != index:
            prev = curr
            curr = curr.next
            node_idx += 1
        
        if curr:
            prev.next = curr.next
            if self.tail == curr:
                self.tail = prev
                # If we have a singleton list, prev will point to the sentinel, which should be changed to point to None
                if self.tail == sentinel:
                    self.tail = None
        
        self.head = sentinel.next
        return
            


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)