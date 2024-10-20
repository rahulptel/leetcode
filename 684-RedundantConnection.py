"""
Reference: https://www.geeksforgeeks.org/union-find/
"""
class Solution:
    def __init__(self):
        self.parents = []
        self.violated = []
        
    def find(self, element):
        """find the set to which the node belongs"""        
        if self.parents[element-1] == -1:
            return element
        else:
            return self.find(self.parents[element-1])
        
    def union(self, set_a, set_b):
        """Join two sets"""
        self.parents[set_b - 1] = set_a
        return
        
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """             
        self.parents = [-1] * len(edges)
        for edge in edges:      
            find_0 = self.find(edge[0])
            find_1 = self.find(edge[1])
            if find_0 == find_1:
                self.violated.append(edge)        
            else:
                self.union(find_0, find_1)
                            
        return self.violated[-1]
