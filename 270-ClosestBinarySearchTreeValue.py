# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        self.min_diff = abs(root.val - target)
        self.min_val = root.val

        def search(node):
            if node:
                diff = node.val - target
                if abs(diff) < self.min_diff:
                    self.min_diff = abs(diff)
                    self.min_val = node.val
                elif abs(diff) == self.min_diff and node.val < self.min_val:
                    self.min_val = node.val                                        
                search(node.left if diff > 0 else node.right)

                
        if root.val - target > 0:
            search(root.left)
        else:
            search(root.right)

        return self.min_val
        
