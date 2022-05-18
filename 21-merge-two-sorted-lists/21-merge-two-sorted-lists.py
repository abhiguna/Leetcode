# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Time = O(M + N), M: len(list1), N: len(list2)
    # Space = O(1)
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode(-math.inf)
        tail = sentinel
        
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                tail = tail.next
                list1 = list1.next 
                tail.next = None
            else:
                tail.next = list2
                tail = tail.next 
                list2 = list2.next 
                tail.next = None
        
        # Gather phase
        if list1:
            tail.next = list1
            tail = tail.next 
        if list2:
            tail.next = list2
            tail = tail.next 
        
        head = sentinel.next 
        return head