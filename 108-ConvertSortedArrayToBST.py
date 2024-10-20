# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def insertTreeNode(nums):            
            mid = len(nums) // 2
            head = TreeNode(nums[mid])
            head.left = insertTreeNode(nums[:mid]) if mid-1 >= 0  else None
            head.right = insertTreeNode(nums[mid+1:]) if mid+1 < len(nums) else None

            return head
        
        root = insertTreeNode(nums)
        return root
