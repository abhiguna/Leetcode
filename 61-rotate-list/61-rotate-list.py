# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Edge case: empty or singleton list
        if not head or not head.next:
            return head
        
        sentinel = ListNode(-math.inf, None)
        tail = sentinel
        
        # Find length of cycle and keep track of the tail of the original list
        length = 0
        curr = head
        while curr:
            length += 1
            tail = curr
            curr = curr.next 
        
        # Find the not rotated part of the list -> (length) - (k % length)
        not_rotated_len = length - (k % length)
        # Check if no net rotations
        if not_rotated_len == length:
            return head# Nothing to do
    
        # Find the rotated part
        pred = None
        rotated = head
        count = 1
        while count <= not_rotated_len:
            count += 1
            pred = rotated
            rotated = rotated.next 
        
        # Modify final list
        tail.next = head
        pred.next = None
        head = rotated

        return head