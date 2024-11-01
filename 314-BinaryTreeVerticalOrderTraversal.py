from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        ROOT_X = 0
        queue = deque([(root, 0)])
        node_store = {}
        sorted_keys = []
                
        while len(queue):
            node, x_pos = queue.popleft()

            if x_pos in node_store:
                node_store[x_pos].append(node.val)
            else:
                node_store[x_pos] = [node.val]

            if node.left is not None:
                queue.append((node.left, x_pos - 1))

            if node.right is not None:
                queue.append((node.right, x_pos + 1))


        return [node_store[xp] for xp in sorted(node_store.keys())]
            
