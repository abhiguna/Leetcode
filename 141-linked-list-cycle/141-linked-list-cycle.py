# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # Time = O(n)
    # Space = O(1)
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        runner_a = head
        runner_b = head.next 
        while runner_a and runner_b and runner_b.next:
            if runner_a == runner_b:
                return True
            runner_a = runner_a.next
            runner_b = runner_b.next.next 
        return False