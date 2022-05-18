# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from heapq import *
import math

class Solution:
    # Time = O(N*klogk), N: the total number of ListNodes
    # Spaxe = O(k)
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        sentinel = ListNode(-math.inf, None)
        tail = sentinel
        min_heap = []
        
        # Add the first k nodes to the min_heap
        for l in lists:
            if l:
                heappush(min_heap, (l.val, id(l), l))
        
        while min_heap:
            (value, _id, node) = heappop(min_heap)
            tail.next = node
            tail = tail.next 
            node = node.next 
            tail.next = None
            # If nodes still exist in the list
            if node:
                heappush(min_heap, (node.val, id(node), node))
        
        # Get the head and return it
        head = sentinel.next 
        return head
    
    
                