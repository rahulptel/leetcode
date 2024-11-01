from collections import defaultdict
"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        visited = set()
        cp, cq = p, q
        while cp is not None or cq is not None:
            if cp is not None:
                if cp.val in visited:
                    return cp
                else:
                    visited.add(cp.val)
                    cp = cp.parent

            if cq is not None:
                if cq.val in visited:
                    return cq
                else:
                    visited.add(cq.val)
                    cq = cq.parent
