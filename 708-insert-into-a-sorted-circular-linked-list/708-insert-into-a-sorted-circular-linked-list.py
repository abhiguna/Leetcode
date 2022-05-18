"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    # Time = O(N)
    # Space = O(1)
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        node = ListNode(insertVal)
        # Edge case 1: empty list given
        if not head:
            node.next = node
            return node
        # Edge case 2: singleton list given
        if head.next == head:
            head.next = node
            node.next = head
            return head
        
        # General case: list of size 2 or more
        # First find the smallest value and the largest value node
        prev = head
        curr = head.next 
        # Check that curr does not proceed beyond 1 loop
        while prev.val <= curr.val and curr != head:
            prev = curr
            curr = curr.next 
        
        # The prev ptr points to the largest value node and the curr ptr points to the smallest value node
        # Treat the list as a non-circular list now
        if insertVal >= prev.val or insertVal <= curr.val:
            prev.next = node
            node.next = curr
            return head
        
        # node will be in the middle of the list
        while insertVal >= curr.val:
            prev = curr
            curr = curr.next 
        
        prev.next = node
        node.next = curr
        return head