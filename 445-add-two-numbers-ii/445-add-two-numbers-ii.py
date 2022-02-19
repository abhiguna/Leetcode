# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Time = O(m + n)
    # Space = O(1)
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_reverse = self.reverseNum(l1)
        l2_reverse = self.reverseNum(l2)
        
        output = ListNode()
        tail = output
        
        carry = 0
        while l1_reverse or l2_reverse:
            val1 = l1_reverse.val if l1_reverse else 0
            val2 = l2_reverse.val if l2_reverse else 0
            new_node = ListNode((carry+val1+val2) % 10)
            carry = (carry+val1+val2) // 10
            tail.next = new_node
            tail = tail.next
            if l1_reverse:
                l1_reverse = l1_reverse.next
            if l2_reverse:
                l2_reverse = l2_reverse.next 
        if carry > 0:
            new_node = ListNode(carry)
            tail.next = new_node
        
        return self.reverseNum(output.next)
    
    def reverseNum(self, llist):
        prev_node = None
        curr_node = llist
        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        return prev_node
            
            
        