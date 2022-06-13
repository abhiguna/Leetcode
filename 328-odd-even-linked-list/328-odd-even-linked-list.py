# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Time = O(n)
    # Space = O(1)
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Edge case: empty or singleton list
        if not head or not head.next:
            return head
        
        # Create two sentinel nodes
        odd_sentinel = ListNode(0)
        o_head, o_tail = odd_sentinel, odd_sentinel
        
        even_sentinel = ListNode(0)
        e_head, e_tail = even_sentinel, even_sentinel
        
        idx = 1
        curr = head
        while curr:
            # Odd idx
            if idx % 2 == 1:
                o_tail.next = curr
                curr = curr.next
                o_tail = o_tail.next 
                o_tail.next = None
            # Even idx
            else:
                e_tail.next = curr
                curr = curr.next
                e_tail = e_tail.next 
                e_tail.next = None
            
            idx += 1
            
        
        o_tail.next = e_head.next 
        return o_head.next 
                
                
        
        