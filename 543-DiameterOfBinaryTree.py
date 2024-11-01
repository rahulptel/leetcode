# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def postOrderTraversal(node):
            if node.left is None and node.right is None:
                node.llong, node.rlong = 0, 0
                return

            node.llong = 0
            if node.left is not None:
                postOrderTraversal(node.left)
                node.llong = max(node.left.llong, node.left.rlong) + 1

            node.rlong = 0
            if node.right is not None:
                postOrderTraversal(node.right)
                node.rlong = max(node.right.llong, node.right.rlong) + 1
            
            if node.llong + node.rlong > self.diameter:
                self.diameter = node.llong + node.rlong

        postOrderTraversal(root)

        return self.diameter
        
