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

    def add_edge(self, edge, cost):
        """ assumes that edge is of type set, tuple or list; 
            between two vertices can be multiple edges! 
        """
        [vertex1, vertex2] = edge
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append((vertex2, cost))
        else:
            self.__graph_dict[vertex1] = [(vertex2, cost)]

    def find_path(self, start_vertex, end_vertex, path=None):
        """ find a path from start_vertex to end_vertex 
            in graph """
        if path == None:
            path = []
        graph = self.__graph_dict
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return path
        if start_vertex not in graph:
            return None
        for (vertex, _) in graph[start_vertex]:
            if vertex not in path:
                extended_path = self.find_path(vertex,
                                               end_vertex,
                                               path)
                if extended_path:
                    return extended_path
        return None

    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        for equation, value in zip(equations, values):
            self.add_vertex(equation[0])
            self.add_vertex(equation[1])

            self.add_edge(equation, value)
            equation.reverse()
            self.add_edge(equation, 1 / value)

        # print(self.__generate_edges())
        result = []
        for query in queries:
            if query[0] not in self.__graph_dict or query[1] not in self.__graph_dict:
                result.append(-1)
            elif query[0] == query[1]:
                result.append(1)
            else:
                path = self.find_path(query[0], query[1])
                if path == None:
                    result.append(-1)
                else:
                    i = 0
                    j = 1
                    cost = 1
                    print(path)
                    while(j < len(path)):
                        for obj in self.__graph_dict[path[i]]:
                            if obj[0] == path[j]:
                                print(obj)
                                cost *= obj[1]
                                break
                        i += 1
                        j += 1
                    result.append(cost)
        return result
