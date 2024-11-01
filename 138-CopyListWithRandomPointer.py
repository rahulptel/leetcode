"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return
        
        node_map = {None: None}
        # Create new nodes and map them to old nodes
        curr = head
        while curr is not None:
            node_map[curr] = Node(curr.val, next=None, random=None)
            curr = curr.next

        # Copy pointer structure from the old nodes to the new nodes
        curr = head
        while curr is not None:
            node_map[curr].next = node_map[curr.next]
            node_map[curr].random = node_map[curr.random]
            curr = curr.next

        return node_map[head]
