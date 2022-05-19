# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Approach 1: Bottom Up DFS
    
    # Time = O(N)
    # Space = O(1)
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Edge case: empty list
        if not head:
            return None
        
        global_head = [None]
        
        def helper(h):
            # Base case: leaf node
            if not h.next:
                global_head[0] = h
                return h
            
            # Recursive case
            succ = helper(h.next)
            succ.next = h
            h.next = None
            return h
        
        helper(head)
        return global_head[0]
            
        
        