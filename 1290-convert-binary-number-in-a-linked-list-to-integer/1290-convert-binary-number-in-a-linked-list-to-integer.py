# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Time = O(N), N: len(linkedlist)
    # Space = O(1)
    def getDecimalValue(self, head: ListNode) -> int:
        total = 0
        
        def find_len(head):
            count = 0
            curr = head
            while curr:
                count += 1
                curr = curr.next
            return count
            
        N = find_len(head)
        power = N - 1
        curr = head
        
        while curr:
            total += curr.val * (2**power)
            power -= 1
            curr = curr.next 
        
        return total