# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Time = O(N), N : length of linkedlist
    # Space = O(1)
    def getDecimalValue(self, head: ListNode) -> int:
        val = 0
        curr = head
        
        # Left shift instead of normal multipication
        while curr:
            val = (val << 1) + curr.val 
            curr = curr.next 
        
        return val