# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        nodes = [root]
        
        while len(nodes) and nodes[0] is not None:
            n = nodes.pop(0)                        
            nodes.append(n.left)            
            nodes.append(n.right)

        while len(nodes) and nodes[0] is None:
            nodes.pop(0)

        return len(nodes) == 0

            
        
