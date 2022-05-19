# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Approach: Top-down DFS
    
    # Time = O(N)
    # Space = O(1)
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Edge case: empty list
        if not head:
            return None
        
        global_head = [None]
        
        def helper(curr, pred):
            # Base case: leaf node
            if not curr.next:
                curr.next = pred
                global_head[0] = curr
                return
            
            succ = curr.next 
            curr.next = pred
            helper(succ, curr)
            return
        
        helper(head, None)
        return global_head[0]