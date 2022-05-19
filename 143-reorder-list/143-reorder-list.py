# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Time = O(N)
    # Space = O(1)
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Edge case: empty list or singleton list
        if not head or not head.next:
            return
        
        # Find the middle node
        hare, tortoise = head, head
        while hare.next and hare.next.next:
            hare = hare.next.next
            tortoise = tortoise.next 
        
        # Reverse the right half
        curr = tortoise.next 
        tortoise.next = None
        pred = None
        while curr:
            succ = curr.next 
            curr.next = pred
            pred = curr
            curr = succ
        
        sentinel = ListNode(-math.inf, None)
        tail = sentinel
        l1, l2 = head, pred
        while l1 and l2:
            # Append l1
            tail.next = l1
            tail = tail.next 
            l1 = l1.next
            tail.next = None
            
            # Append l2
            tail.next = l2
            tail = tail.next 
            l2 = l2.next 
            tail.next = None

        # If list has odd num of elements, there will be 1 extra element in the left half
        tail.next = l1
        head = sentinel.next 
        return
        
        