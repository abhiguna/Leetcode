# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Time = O(N)
    # Space = O(1)
    
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # Visualize as Left------[middle (to be reversed)]------Right
        # Create a sentinel node to keep track of the updated head
        sentinel = ListNode(-math.inf, head)
        pred = sentinel
        curr = head
        idx = 1
        # Find the start of the middle portiom
        while idx != left:
            idx += 1
            pred = curr
            curr = curr.next 
            
        tail_left = pred
        tail_middle = curr # This will be the tail after the reversal
        
        pred.next = None
        pred = None
        
        # Reverse the middle sublist
        while idx != right + 1:
            idx += 1
            succ = curr.next 
            curr.next = pred
            pred = curr
            curr = succ
        
        head_middle = pred
        head_right = curr
        
        tail_left.next = head_middle
        tail_middle.next = head_right
        
        final_head = sentinel.next
        return final_head
        