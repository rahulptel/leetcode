"""Make it faster
"""
import collections

class Solution:
    def __init__(self, graph_dict=None):
        """ initializes a graph object 
            If no dictionary or None is given, 
            an empty dictionary will be used
        """
        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict
        
    def vertices(self):
        """ returns the vertices of a graph """
        return list(self.__graph_dict.keys())

    def edges(self):
        """ returns the edges of a graph """
        return self.__generate_edges()

    def __generate_edges(self):
        """ A static method generating the edges of the 
            graph "graph". Edges are represented as sets 
            with one (a loop back to the vertex) or two 
            vertices 
        """
        edges = []
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges

    def add_vertex(self, vertex):
        """ If the vertex "vertex" is not in 
            self.__graph_dict, a key "vertex" with an empty
            list as a value is added to the dictionary. 
            Otherwise nothing has to be done. 
        """
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []

    def add_edge(self, edge):
        """ assumes that edge is of type set, tuple or list; 
            between two vertices can be multiple edges! 
        """
        [vertex1, vertex2] = edge
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
        else:
            self.__graph_dict[vertex1] = [vertex2]
                    
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # Construct graph
        for course in range(numCourses):
            self.add_vertex(course)            
        for prereq in prerequisites:
            prereq.reverse()
            self.add_edge(prereq)
                
        # DFS over the graph and check for cycles
        WHITE, GRAY, BLACK = 0, 1, 2        
        color = collections.defaultdict(int)
        visited = []
        
        def dfs(node):
            if color[node] != WHITE:
                return color[node] == BLACK

            color[node] = GRAY
            visited.append(node)
            for neighbour in self.__graph_dict[node]:
                if color[neighbour] == BLACK:
                    continue
                elif neighbour not in visited:
                    if dfs(neighbour) == False:
                        return False
                elif neighbour in visited and color[neighbour] == GRAY:
                    print(node, neighbour)
                    return False
                    
            color[node] = BLACK
            return True
            
        return True if len(list(filter(dfs, range(len(self.__graph_dict))))) == numCourses else False
        
        
