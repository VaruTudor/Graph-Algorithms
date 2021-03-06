from errors import CompleteGraph, AlreadyExists, EdgeNotFount
import random

class DictGraph:
    
    def __init__(self):
        """
            Creates a graph using dictionaries
        """
        self.n = 0  # the number of vertices
        self.m = 0  # the number of edges
        self.D_out = {} 
        self.D_in = {}  
        self.D_cost = {}    # dictionary of edges costs

        # f = open(file_name,'r')
        # line = f.readline()
        # line = line.split(' ')
        # self.n = int(line[0])
        # self.m = int(line[1])
        # self.D_in = {}
        # self.D_out = {}
        # self.D_cost = {}
        # for i in range(self.n):
        #     self.D_out[i] = []
        #     self.D_in[i] = []

        # while True:
        #     line = f.readline()
        #     if len(line) == 0:
        #         return
        #     line = line[:-1]
        #     line = line.split(' ')
        #     v1 = int(line[0])
        #     v2 = int(line[1])
        #     cost = int(line[2])
        #     self.D_out[v1].append(v2) 
        #     self.D_in[v2].append(v1)
        #     self.D_cost[(v1,v2)] = cost

    def outbound_edges(self,x):
        """
            returns the outbound edges of a vertex
            x - vertex (int)
        """
        edges = []
        for e in self.D_cost.keys():
            if e[0] == x:
                edges.append(e)
        return edges
    
    def inbound_edges(self,x):
        """
            returns the outbound edges of a vertex
            x - vertex (int)
        """
        edges = []
        for e in self.D_cost.keys():
            if e[1] == x:
                edges.append(e)
        return edges

    def read_file(self, file_name):
        """
            Reads a graph from a file
            file_name - the name of the file (string)
        """
        f = open(file_name,'r')
        line = f.readline()
        line = line.split(' ')
        self.n = int(line[0])
        self.m = int(line[1])

        for i in range(self.n):
            self.D_out[i] = []
            self.D_in[i] = []

        while True:
            line = f.readline()
            if len(line) == 0:
                return
            line = line[:-1]
            line = line.split(' ')
            v1 = int(line[0])
            v2 = int(line[1])
            cost = int(line[2])
            self.D_out[v1].append(v2) 
            self.D_in[v2].append(v1)
            self.D_cost[(v1,v2)] = cost

    def remove_vertex(self, x):
        """
            removes a vertex from the graph
            x - the vertex to be removed
        """
        # this might work as well
        del(self.D_out[x])
        del(self.D_in[x])
        for e in list(self.D_cost):
            if x in e:
                del(self.D_cost[e])
        for v in self.D_out:
            try:
                self.D_out[v].remove(x)
            except ValueError:
                continue
        for v in self.D_in:
            try:
                self.D_in[v].remove(x)
            except ValueError:
                continue
        """
        for v in self.D_out[x]:
            # D.out[x] contains all edges leaving the x vertex
            for e in list(self.D_cost):
                if e[1] == v:
                    self.D_in[e[1]].remove(e[0])
                    del(self.D_cost[e])
        for v in self.D_out:
            try:
                self.D_out[v].remove(x)
            except ValueError:
                continue
        del(self.D_out[x])
        del(self.D_in[x])
        """

    def get_cost(self, x, y):
        """
            returns the cost of an edge
            x - first vertex (int)
            y - second vertex (int)
        """
        self.isEdge(x,y)
        if (x,y) not in self.D_cost.keys():
            raise EdgeNotFount
        return self.D_cost[(x,y)]

    def modify_cost(self, x, y, new_cost):
        """
            modifies the cost of an edge
            x - first vertex (int)
            y - second vertex (int)
            new_cost - the updated cost (int)
        """
        self.isEdge(x,y)
        if (x,y) not in self.D_cost.keys():
            raise EdgeNotFount
        self.D_cost[(x,y)] = new_cost

    def isEdge(self, x, y):
        """
            x, y - vertices
            return  - True if there is an edge
                    - False if there is not an edge
        """
        if y not in self.D_in.keys():
            raise ValueError
        if x not in self.D_out.keys():
            raise ValueError
        return x in self.D_in[y] and y in self.D_out[x]

    def inDegree(self, x):
        """
            returns the in degree of a vertex
            x - the vertex (int)
        """
        if x not in self.D_out.keys():
            raise ValueError
        return len(self.D_in[x])
    
    def outDegree(self, x):
        """
            returns the out degree of a vertex
            x - the vertex (int)
        """
        if x not in self.D_out.keys():
            raise ValueError
        return len(self.D_out[x])

    def addEdge(self, x, y, cost):
        """
            Checks if x and y exist as vertices and adds an edge if such
            If x and y don't exist as vertices the fuction returns None
            x - first vertex (int)
            y - second vertex (int)
            cost - the cost (int)
        """
        if self.m == (self.n * (self.n - 1)) / 2:
            raise CompleteGraph
        if self.isEdge(x,y) == False:
            return AlreadyExists
        self.D_in[y].append(x)
        self.D_out[x].append(y)
        self.D_cost[(x,y)] = cost
        self.m += 1
    
    def removeEdge(self, x, y):
        """
            Removes an edge if it exist (else raise ValueError)
        """
        if self.isEdge(x,y) == False:
            raise ValueError
        self.D_out[x].remove(y)
        self.D_cost.pop((x,y))
        self.D_in[y].remove(x)
        self.m -= 1

    def add_vertex(self):
        """
            adds a vertex to the graph
        """
        self.D_in[len(self.D_in)] = []
        self.D_out[len(self.D_out)] = []
        self.n += 1

    def nrVertices(self):
        """
            returns the number of vertices
        """
        return len(self.D_out)

    def vertices(self):
        """
            returns the vetices as a list
        """
        l = []
        for i in self.D_in.keys():
            l.append(i)
        return l

    def copy_graph(self, new_graph):
        """
            copies the graph to a new one
            new_graph - a new copy of the graph (DictGraph)
        """
        if (type(new_graph)!=DictGraph)
            raise ValueError
        new_graph.n = self.n
        new_graph.m = self.m
        new_graph.D_in = self.D_in.copy()
        new_graph.D_out = self.D_out.copy()
        new_graph.D_cost = self.D_cost.copy()

### external functions ###

def write_graph_external(graph, file_name):
    """
        writes the graph with the correspondig format in a file
        graph - the graph where the data is inserted (DictGraph)
        file_name - the name of the file (str)
    """
    f = open(file_name,"w")
    first_line = str(graph.n) + ' ' + str(graph.m)
    f.write(first_line)
    lines = []
    for edge in graph.D_cost:
        line = str(edge[0]) + ' ' + str(edge[1]) + ' ' + str(graph.D_cost[edge])
        lines.append(line)
    f.writelines(lines)
    f.close()

def read_graph_external(graph, file_name):
    """
        reads the graph with the correspondig format from a file
        graph - the graph where the data is inserted (DictGraph)
        file_name - the name of the file (str)
    """
    f = open(file_name,'r')
    line = f.readline()
    line = line.split(' ')
    graph.n = int(line[0])
    graph.m = int(line[1])

    for i in range(graph.n):
        graph.D_out[i] = []
        graph.D_in[i] = []

    while True:
        line = f.readline()
        if len(line) == 0:
            return
        line = line[:-1]
        line = line.split(' ')
        v1 = int(line[0])
        v2 = int(line[1])
        cost = int(line[2])
        graph.D_out[v1].append(v2) 
        graph.D_in[v2].append(v1)
        graph.D_cost[(v1,v2)] = cost

    f.close()

def create_random_graph(no_vertices, no_edges):
    """
        creates a random graph
        no_verices - number of vertices (int)
        no_edges - (int)
    """
    graph = DictGraph()

    for i in range(no_vertices):
        graph.n += 1
        graph.D_in[i] = []
        graph.D_out[i] = []

    while graph.m != no_edges:
        v1 = random.randrange (0,no_vertices,1)
        v2 = random.randrange (0,no_vertices,1)
        cost = random.randrange (-9999,9999,1)
        graph.addEdge(v1,v2,cost)

    return graph


### ### ###