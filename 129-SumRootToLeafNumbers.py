# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.total = 0

        def dfs(node, local_sum):
            if node:
                local_sum = local_sum * 10 + node.val
                dfs(node.left, local_sum)
                dfs(node.right, local_sum)
                if node.left is None and node.right is None:
                    self.total += local_sum

        dfs(root, 0)
        return self.total
        
