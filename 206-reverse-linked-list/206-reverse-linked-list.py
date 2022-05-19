# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Approach: iterative version
    
    # Time = O(N)
    # Space = O(1)
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Edge case: empty or singleton list
        if not head or not head.next:
            return head
        
        curr = head
        pred = None
        while curr:
            succ = curr.next 
            curr.next = pred
            pred = curr
            curr = succ
            
        # The pred ptr points to the head of the reversed list
        return pred