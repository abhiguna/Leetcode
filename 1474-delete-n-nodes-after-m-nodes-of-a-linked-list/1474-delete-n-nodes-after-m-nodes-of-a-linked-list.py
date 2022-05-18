# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Time = O(N)
    # Space = O(1)
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        sentinel = ListNode(-math.inf, head)
        prev, curr = sentinel, head
        while curr:
            steps = 1
            # Move curr forward M steps
            while curr and steps <= m:
                prev = curr
                curr = curr.next 
                steps += 1
            
            # Check if curr goes out of bounds
            if not curr: 
                break
            
            # Move forward N steps
            p = curr
            steps = 1
            while p and steps <= n:
                p = p.next 
                steps += 1
            
            prev.next = p
            curr = p
    
        return head
            
            