# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Time = O(N^2)
    # Space = O(1)
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode(-math.inf, None)
        curr = head
        while curr:
            # Extract the curr node from the unsorted list
            succ = curr.next 
            curr.next = None
            # Insert it into sorted list
            pred = sentinel
            curr2 = sentinel.next
            # The right half of the sorted list pointed to by the sentinel node will be sorted after each iteration
            while curr2 and curr2.val <= curr.val:
                pred = curr2
                curr2 = curr2.next 
            # Found the insertion location
            pred.next = curr 
            curr.next = curr2
            
            # Consider the next element in the unsorted list
            curr = succ
        
        head = sentinel.next 
        return head