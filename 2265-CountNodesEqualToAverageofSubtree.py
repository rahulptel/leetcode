# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.counter = 0
        def traverse(node):
            if node.left is None and node.right is None:
                self.counter += 1
                return node.val, 1

            sum_ = node.val
            count_ = 1
            if node.left is not None:
                sumLeft, countLeft = traverse(node.left)
                sum_ += sumLeft
                count_ += countLeft

            if node.right is not None:
                sumRight, countRight = traverse(node.right)
                sum_ += sumRight
                count_ += countRight

            if int(sum_ / count_) == node.val:
                self.counter += 1

            return sum_, count_

        traverse(root)
            
        return self.counter
        
