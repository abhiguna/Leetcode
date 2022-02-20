# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        
        # Find the middle node
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse the second part of the list
        prev_node = None
        curr_node = slow
        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        
        # Merge the two sorted lists
        first = head
        second = prev_node
        while second.next:
            temp_node = first.next
            first.next = second
            first = temp_node
            
            temp_node = second.next
            second.next = first
            second = temp_node
            
        
            