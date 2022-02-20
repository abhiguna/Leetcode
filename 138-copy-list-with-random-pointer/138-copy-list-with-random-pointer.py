"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

from collections import defaultdict

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        output = Node(0)
        tail = output
        
        node_dict = defaultdict()
        curr_node = head
        
        while curr_node:
            if curr_node not in node_dict:
                new_node = Node(curr_node.val)
                node_dict[curr_node] = new_node
            else:
                new_node = node_dict[curr_node]
            tail.next = new_node
            tail = tail.next
            if curr_node.next and curr_node.next not in node_dict:
                next_node = Node(curr_node.next.val)
                node_dict[curr_node.next] = next_node
            elif curr_node.next in node_dict:
                next_node = node_dict[curr_node.next]
            else:
                next_node = None
            new_node.next = next_node
            if curr_node.random and curr_node.random not in node_dict:
                random_node = Node(curr_node.random.val)
                node_dict[curr_node.random] = random_node
            elif curr_node.random in node_dict:
                random_node = node_dict[curr_node.random]
            else:
                random_node = None
            new_node.random = random_node
            
            curr_node = curr_node.next
            
        return output.next
            