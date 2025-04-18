# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def checkMirror(n1, n2):
            if n1 is None and n2 is None:
                return True

            elif n1 is None or n2 is None:
                return False

            return n1.val == n2.val and \
                checkMirror(n1.left, n2.right) and \
                checkMirror(n1.right, n2.left)
            

        if root is None:
            return True

        
        return checkMirror(root.left, root.right)        
        
