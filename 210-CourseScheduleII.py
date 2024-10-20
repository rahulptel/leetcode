"""Need to improve speed
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
        self.__inv_graph_dict = {}
        
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
        
        if vertex not in self.__inv_graph_dict:
            self.__inv_graph_dict[vertex] = []

            
    def add_edge(self, edge):
        """ assumes that edge is of type set, tuple or list; 
            between two vertices can be multiple edges! 
        """
        [vertex1, vertex2] = edge
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
        else:
            self.__graph_dict[vertex1] = [vertex2]
        
        if vertex2 in self.__inv_graph_dict:
            self.__inv_graph_dict[vertex2].append(vertex1)
        else:
            self.__inv_graph_dict[vertex2] = [vertex1]
        
        
            
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """                
        # Construct graph
        for course in range(numCourses):
            self.add_vertex(course)            
        not_parents = []
        for prereq in prerequisites:
            if prereq[0] == prereq[1]:
                return []
            not_parents.append(prereq[0])
            prereq.reverse()
            self.add_edge(prereq)

        
        parents = list(set([course for course in range(numCourses)]).difference(not_parents))
        process = []
        for parent in parents:
            process.extend(self.__graph_dict[parent])
        process = list(set(process))
        
        # Find schedule        
        while len(process):
            flag = 0
            for idx, node in enumerate(process):
                if set(self.__inv_graph_dict[node]).issubset(parents):                    
                    flag = 1
                    parents.append(node)
                    new_nodes = self.__graph_dict[node]
                    process.pop(idx)
                    process.extend(new_nodes)                                        
                    process = list(set(process))                    
                    break
            if flag == 0:
                return []
                        
        return parents if len(parents) == numCourses else []
        
        
        
