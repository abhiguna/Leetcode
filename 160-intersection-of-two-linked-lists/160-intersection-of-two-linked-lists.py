# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # Time = O(m + n) -> m = len(listA), n = len(listB)
    # Space = O(m) 
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        seen_nodes = set()
        runner_a = headA
        runner_b = headB
        
        while runner_a:
            seen_nodes.add(runner_a)
            runner_a = runner_a.next 
        
        while runner_b:
            if runner_b in seen_nodes:
                return runner_b
            runner_b = runner_b.next 
        
        return None