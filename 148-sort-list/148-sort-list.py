# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Time = O(NlogN)
    # Space = O(1) explicit aux. space
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def merge_lists(l1, l2):
            sentinel = ListNode(-math.inf)
            tail = sentinel
            
            while l1 and l2:
                if l1.val <= l2.val:
                    tail.next = l1
                    tail = l1
                    l1 = l1.next 
                    tail.next = None
                else:
                    tail.next = l2
                    tail = l2
                    l2 = l2.next 
                    tail.next = None
            if l1:
                tail.next = l1
                tail = tail.next 
            if l2:
                tail.next = l2
                tail = tail.next 
            
            head = sentinel.next 
            return head
        
        def merge_sort(head):
            # Edge case: empty list or a singleton list
            if not head or not head.next:
                return head
            
            # Find the middle
            hare, tortoise = head, head
            while hare.next and hare.next.next:
                hare = hare.next.next
                tortoise = tortoise.next 
            
            h1 = head
            h2 = tortoise.next 
            tortoise.next = None
            l1 = merge_sort(h1)
            l2 = merge_sort(h2)
            return merge_lists(l1, l2)
        
        return merge_sort(head)    