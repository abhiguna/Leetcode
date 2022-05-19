# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Time = O(N)
    # Space = O(1)
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        sentinel = ListNode(-math.inf, head)
        tail = sentinel
        
        curr = head
        while curr:
            # Reverse the next k nodes and the hand over the remaining nodes to subordinates
            # m is the messenger node that points to the remaining subproblem
            m = curr
            for _ in range(k):
                # If m is null, then we know we have less than k nodes remaining, so return the list as it is now
                if not m:
                    head = sentinel.next
                    return head
                m = m.next 
            
            # Reverse the k nodes upto m 
            pred = None
            sub_tail = curr # the curr node will be the tail of the sublist
            
            while curr != m:
                succ = curr.next 
                curr.next = pred
                pred = curr
                curr = succ
            
            # pred points to the head of the reversed sublist
            tail.next = pred
            sub_tail.next = m
            
            tail = sub_tail
            curr = m
    
        head = sentinel.next
        return head
            