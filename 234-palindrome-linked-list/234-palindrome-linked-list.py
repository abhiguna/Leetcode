# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Time = O(N)
    # Space = O(1)
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Edge case: empty or singleton list
        if not head or not head.next:
            return True
        
        # Find the middle node
        hare, tortoise = head, head
        while hare.next and hare.next.next:
            hare = hare.next.next
            tortoise = tortoise.next 
        
        # Reverse the right half (tortoise points to the tail of the left half)
        tail_left = tortoise
        curr = tortoise.next
        tail_left.next = None 
        pred = None
        while curr:
            succ = curr.next 
            curr.next = pred
            pred = curr
            curr = succ
        
        # Validate palindrome and do cleanup on the input
        left = head
        curr = pred
        pred = None
        answer = True
        while curr:
            # Check palindrome or not
            if left.val != curr.val:
                answer = False
            left = left.next
            succ = curr.next 
            curr.next = pred
            pred = curr
            curr = succ
        
        tail_left.next = pred
        return answer