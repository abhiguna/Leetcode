# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Time = O(min(m, n)) --> m = len(l1), n = len(l2)
    # Space = O(1)
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        output = ListNode()
        tail = output
        
        carry = 0
        while l1 and l2:
            digit_sum = carry + l1.val + l2.val
            carry = digit_sum // 10
            new_node = ListNode(digit_sum % 10)
            tail.next = new_node
            tail = tail.next 
            l1 = l1.next 
            l2 = l2.next
        
        while l1:
            digit_sum = carry + l1.val
            carry = digit_sum // 10
            new_node = ListNode(digit_sum % 10)
            tail.next = new_node
            tail = tail.next 
            l1 = l1.next 
        while l2:
            digit_sum = carry + l2.val
            carry = digit_sum // 10
            new_node = ListNode(digit_sum % 10)
            tail.next = new_node
            tail = tail.next 
            l2 = l2.next 
        
        if carry > 0:
            new_node = ListNode(carry)
            tail.next = new_node
            tail = tail.next
        
        return output.next
        