# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        self.max_depth = 0

        def dfs(node, depth):
            if node is None:
                return

            if self.max_depth < depth:                
                self.max_depth = depth
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)                

        dfs(root, 1)
        return self.max_depth
