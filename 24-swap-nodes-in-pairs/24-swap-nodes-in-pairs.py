# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Time = O(n), n: # of nodes in the list
    # Space = O(1)
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Edge case: empty list or singleton list
        if not head or not head.next:
            return head
        
        # General case: we have atleast two nodes to reverse
        sentinel = ListNode(0, head)
        prev = sentinel
        curr = head
        
        while curr and curr.next:
            # Store the pointers
            second = curr.next
            nxt_pair = curr.next.next 
            
            # Reverse the current pair of nodes
            curr.next = nxt_pair
            second.next = curr
            
            # Update pointers
            prev.next = second
            prev = curr
            curr = nxt_pair
        
        return sentinel.next