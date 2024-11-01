# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.counter = 0        

        def inorder_traversal(node):
            if node:
                if low <= node.val <= high:
                    self.counter += node.val
                    inorder_traversal(node.left)
                    inorder_traversal(node.right)
                elif node.val < low:
                    inorder_traversal(node.right)
                else:
                    inorder_traversal(node.left)
        
        inorder_traversal(root)

        return self.counter
        
