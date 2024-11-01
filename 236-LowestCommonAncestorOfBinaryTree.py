# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.lca = None

        def postorder(node):   
            if node is None:
                return False

            left_anc = postorder(node.left)
            right_anc = postorder(node.right)
            curr_anc = node.val == p.val or node.val == q.val
            if (left_anc and right_anc) or (curr_anc and left_anc) or (curr_anc and right_anc):
                self.lca = node
                return True

            return left_anc or right_anc or curr_anc
            
        postorder(root)
        return self.lca

        

        
