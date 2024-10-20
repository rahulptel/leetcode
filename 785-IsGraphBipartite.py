"""Imporve on speed
"""
class Solution:
    def __init__(self):
        self.NOT_COLORED = 0
        self.COLOR_1 = 1
        self.COLOR_2 = -1
        self.INV_COLOR = -1
                
    def color_nodes(self, start_node, graph):  
        # Color the source node
        self.colored[start_node] = self.COLOR_1
        
        # BFS on graph from start_node
        queue = [start_node]
        while len(queue):
            current_node = queue.pop(0)              
            for neighbour in graph[current_node]:
                # Check for self loop
                if neighbour == current_node:
                    return False
                # Neighbour not colored
                elif self.colored[neighbour] == self.NOT_COLORED:
                    self.colored[neighbour] = self.INV_COLOR * self.colored[current_node]
                    queue.append(neighbour)
                # Check that the neighbour doesn't have the same color as the parent                    
                elif self.colored[neighbour] == self.colored[current_node]:
                    return False        
        return True
        
        
        
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """        
        self.colored = [self.NOT_COLORED] * len(graph)
        for vertex, _ in enumerate(graph):
            if self.colored[vertex] == self.NOT_COLORED:
                if self.color_nodes(vertex, graph) == False:
                    return False        
        return True
