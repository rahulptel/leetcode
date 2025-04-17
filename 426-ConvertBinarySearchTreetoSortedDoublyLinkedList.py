"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        self.head = None
        self.curr = None
        if root is None:
            return self.head

        def dfs(node):
            if node.left is None and node.right is None:
                new_node = Node(node.val, left=None, right=None)
                if self.head is None:
                    self.head = new_node
                    self.curr = new_node
                else:
                    self.curr.right = new_node
                    new_node.left = self.curr
                    self.curr = new_node
                return


            if node.left is not None:
                dfs(node.left)

            new_node = Node(node.val, left=None, right=None)
            if self.head is None:
                self.head = new_node
                self.curr = new_node
            else:
                self.curr.right = new_node
                new_node.left = self.curr
                self.curr = new_node

            if node.right is not None:
                dfs(node.right)
        
        dfs(root)
        self.head.left = self.curr
        self.curr.right = self.head

        return self.head


        
