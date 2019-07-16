#!python

""" Vertex Class
A helper class for the Graph class that defines vertices and vertex neighbors.
"""


class Vertex(object):

    def __init__(self, vertex):
        """initialize a vertex and its neighbors

        neighbors: set of vertices adjacent to self,
        stored in a dictionary with key = vertex,
        value = weight of edge between self and neighbor.
        """
        self.id = vertex
        self.neighbors = {}

    def addNeighbor(self, vertex, weight=0):
        """add a neighbor along a weighted edge"""
        #if vertex is not already a neighbor add vertex and assign weight
        if vertex not in self.neighbors:
            self.neighbors[vertex] = weight

    def __str__(self):
        """output the list of neighbors of this vertex"""
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.neighbors])

    def getNeighbors(self):
        """return the neighbors of this vertex"""
        return self.neighbors.keys()

    def getId(self):
        """return the id of this vertex"""
        return self.id

    def getEdgeWeight(self, vertex):
        """return the weight of this edge from this vertex to the given vertex."""
        return self.neighbors[vertex]
 


""" Graph Class
A class demonstrating the essential
facts and functionalities of graphs.
"""


class Graph:
    def __init__(self):
        """ initializes a graph object with an empty dictionary.
        """
        self.vertList = {}
        self.numVertices = 0
        self.numEdges = 0

    def addVertex(self, key):
        """add a new vertex object to the graph with
        the given key and return the vertex
        """
        #increment the number of vertices
        self.numVertices += 1
        #create a new vertex
        vertex = Vertex(key)
        #add the new vertex to the vertex list
        self.vertList[key] = vertex
        #return the new vertex
        return vertex

    def getVertex(self, n):
        """return the vertex if it exists"""
        return n if self.vertList[n] else None
        

    def addEdge(self, f, t, cost=0):
        """add an edge from vertex f to vertex t with a cost
        """
        #if either vertex is not in the graph, return error
        if not self.vertList[f]:
            self.addVertex(f)
        elif not self.vertList[t]:
            self.addVertex(t)
        #if both vertices in the graph, make t a neighbor of f
        else:
            self.numEdges+=1
            self.vertList[t].addNeighbor(self.vertList[f], cost)

    def getVertices(self):
        """return all the vertices in the graph"""
        return self.vertList.keys()

    def __iter__(self):
        """iterate over the vertex objects in the
        graph, to use sytax: for v in g
        """
        return iter(self.vertList.values())
    
    def countVertices(self):
        '''counts number of vertices
        '''
        return self.numVertices
    
    def countEdges(self):
        '''counts number of edges
        '''
        return self.numEdges

def get_data(file):
    '''reading in data from file to create a graph
    '''
    with open(file) as f:
        data = f.read().split()
    return data

def create_graph(data):
    '''takes in data and creates graph w/ vertices and edges
    '''
    graph = Graph()

    for vertex in data[1].split(','):
        graph.addVertex(vertex)
    
    for item in data[2:]:
        graph.addEdge(item[1], item[3], item[5:].replace(')', ''))


    print("The edges are: ")
    for vertex in graph:
        for w in vertex.getNeighbors():
            print("( %s , %s )" % (vertex.getId(), w.getId()))
    
    print("The number of edges are: ", graph.countEdges(), "\n")
    
    print("The number of vertices are: ", graph.countVertices(), "\n")
    # Print vertices
    print("The vertices are: ", graph.getVertices(), "\n")


# Driver code


if __name__ == "__main__":

    # Challenge 1: Create the graph

    g = Graph()

    # Add your friends
    g.addVertex("Ebonne")
    g.addVertex("Nadia")
    g.addVertex("Billy")
    g.addVertex("Julian")
    g.addVertex("Tonya")
    g.addVertex("Kenny")
    g.addVertex("Domonique")
    g.addVertex("Ravin")
    g.addVertex("Neffie")
    g.addVertex("Vitaline")


    # ...  add all 10 including you ...

    # Add connections (non weighted edges for now)
    g.addEdge("Ebonne", "Nadia")
    g.addEdge("Nadia", "Billy")
    g.addEdge("Billy", "Julian")
    g.addEdge("Julian", "Nadia")
    g.addEdge("Ebonne", "Tonya")
    g.addEdge("Tonya", "Kenny")
    g.addEdge("Kenny", "Domonique")
    g.addEdge("Domonique", "Ravin")
    g.addEdge("Ravin", "Vitaline")
    g.addEdge("Vitaline", "Tonya")
    g.addEdge("Ebonne", "Neffie")
    g.addEdge("Tonya", "Neffie")

    # Challenge 1: Output the vertices & edges
    # Print vertices
    print("The vertices are: ", g.getVertices(), "\n")

    print("The edges are: ")
    for v in g:
        for w in v.getNeighbors():
            print("( %s , %s )" % (v.getId(), w.getId()))
    

    data = get_data('graph.txt')
    graph = create_graph(data)