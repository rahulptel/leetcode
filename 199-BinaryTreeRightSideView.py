# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        prev = []
        curr = [root]
        result = []

        if root is None:
            return []        

        while len(curr):
            last = curr[-1]
            result.append(last.val)

            prev = curr
            curr = []
            for n in prev:
                if n.left is not None:
                    curr.append(n.left)
                if n.right is not None:
                    curr.append(n.right)

        return result

        
