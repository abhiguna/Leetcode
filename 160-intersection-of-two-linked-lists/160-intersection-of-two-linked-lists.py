# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # Time = O(m + n) -> m = len(listA), n = len(listB)
    # Space = O(1) 
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        runner_a = headA
        runner_b = headB
        
        while runner_a != runner_b:
            runner_a = headB if not runner_a else runner_a.next
            runner_b = headA if not runner_b else runner_b.next 
        
        return runner_a