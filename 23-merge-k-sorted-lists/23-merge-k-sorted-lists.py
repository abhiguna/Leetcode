# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Time = O(klogk + N), k: len(lists), N: # of nodes in all the linkedlists
    # Space = O(k)
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)
        
        sentinel = ListNode()
        head, tail = sentinel, sentinel
        
        min_heap = []
        
        # Insert the first k nodes into the min_heap
        for i in range(k):
            # If list is not empty
            if lists[i]:
                heappush(min_heap, (lists[i].val, id(lists[i]), lists[i]))
        
        while min_heap:
            (val, _id, node) = heappop(min_heap)
            # Append to merged list
            tail.next = node
            tail = tail.next
            node = node.next
            
            if node:
                heappush(min_heap, (node.val, id(node), node))
        
        head = head.next
        return head
                    
                    
                    