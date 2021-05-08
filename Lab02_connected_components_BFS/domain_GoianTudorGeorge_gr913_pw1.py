from errors_GoianTudorGeorge_gr913_pw1 import CompleteGraph, AlreadyExists, EdgeNotFount, NotExistentVertex
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
        if self.isEdge(x,y) == True:
            raise AlreadyExists
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
        if (type(new_graph)!=DictGraph):
            raise ValueError
        new_graph.n = self.n
        new_graph.m = self.m
        new_graph.D_in = self.D_in.copy()
        new_graph.D_out = self.D_out.copy()
        new_graph.D_cost = self.D_cost.copy()

    def bfs_forward(self, start_vertex, end_vertex):
        """
            searches a bfs path forward
            input:
                start_vertex - the vertex from where the search starts
                end_vertex - a vertex where the search ends
            return:
                lowest length path between starting_vertex and end_vertex
        """
        if start_vertex not in self.D_in.keys() or end_vertex not in self.D_in.keys():
            raise NotExistentVertex
        queue = list()
        previous = dict()
        distance = dict()
        visited = set()
        queue.append(start_vertex)
        visited.add(start_vertex)
        distance[start_vertex] = 0
        while len(queue) != 0:
            x = queue.pop()
            for n in self.D_out[x]:
                if n not in visited:
                    queue.append(n)
                    visited.add(n)
                    distance[n] = distance[x] + 1
                    if n == end_vertex:
                        return distance[n]
                    previous[n] = x
        return 0

    def bfs_backward(self, start_vertex, end_vertex):
        """
            searches a bfs path backward
            input:
                start_vertex - the vertex from where the search starts
                end_vertex - a vertex where the search ends
            return:
                lowest length path between starting_vertex and end_vertex
        """
        if start_vertex not in self.D_in.keys() or end_vertex not in self.D_in.keys():
            raise NotExistentVertex
        queue = list()
        previous = dict()
        distance = dict()
        visited = set()
        queue.append(end_vertex)
        visited.add(end_vertex)
        distance[end_vertex] = 0
        while len(queue) != 0:
            x = queue.pop()
            for n in self.D_in[x]:
                if n not in visited:
                    queue.append(n)
                    visited.add(n)
                    distance[n] = distance[x] + 1
                    if n == end_vertex:
                        return distance[n]
                    previous[n] = x
        return 0

### undirected graph ###

class UndirectedGraph:
    def __init__(self):
        """
            Creates a graph using dictionaries
        """
        self.n = 0  # the number of vertices
        self.m = 0  # the number of edges
        self.D_vertices = {} 

    def __str__(self):
        s = "\nvertices: "
        n = "\nedges: "
        for v in self.D_vertices:
            s += str(v)+"  "
            for k in self.D_vertices[v]:
                n += "( "+ str(v) + "  " + str(k) + " ) "
        
        s += n

        return s

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
            self.D_vertices[i] = []

        while True:
            line = f.readline()
            if len(line) == 0:
                return
            line = line[:-1]
            line = line.split(' ')
            v1 = int(line[0])
            v2 = int(line[1])
            self.D_vertices[v1].append(v2) 
            self.D_vertices[v2].append(v1)

    def isEdge(self, x, y):
        """
            x, y - vertices
            return  - True if there is an edge
                    - False if there is not an edge
        """
        if x not in self.D_vertices.keys() or y not in self.D_vertices.keys():
            raise ValueError
        return x in self.D_vertices[y] and y in self.D_vertices[x]

    def addEdge(self, x, y):
        """
            Checks if x and y exist as vertices and adds an edge if such
            If x and y don't exist as vertices the fuction returns None
            x - first vertex (int)
            y - second vertex (int)
            cost - the cost (int)
        """
        # if self.m != 0 and self.m != self.n*(self.n-1):
        #     return CompleteGraph
        if self.isEdge(x,y) == True:
            return
        self.D_vertices[y].append(x)
        self.D_vertices[x].append(y)
        self.m += 1

    def add_vertex(self):
        """
            adds a vertex to the graph
        """
        self.D_vertices[len(self.D_vertices)] = []
        self.n += 1

    def add_specific_vertex(self, vertex):
        """
            adds a vertex to the graph
        """
        if self.m != 0 and self.m != self.n*(self.n-1):
            return CompleteGraph
        self.D_vertices[vertex] = []
        self.n += 1

    
    # A function used by DFS 
    def dfs_util(self, v, visited, connected_component): 
  
        # Mark the current node as visited  
        # and add it to the current connected componenet
        visited[v] = True
        connected_component.append(v)
  
        # Recur for all the vertices  
        # adjacent to this vertex 
        for i in self.D_vertices[v]: 
            if visited[i] == False: 
                self.dfs_util(i, visited, connected_component) 

    # The function to do DFS traversal. It uses 
    # recursive dfs_util() 
    def dfs(self, v): 
  
        connected_component = list()

        # Mark all the vertices as not visited 
        visited = [False] * (len(self.D_vertices)) 
  
        # Call the recursive helper function  
        self.dfs_util(v, visited, connected_component)

        return connected_component 

    def find_connencted_components_dfs(self):
        """
            finds all connected components
            return:
                connencted_components - (list) contains dictionaries of connected components
        """
        # first we choose the starting vertex
        start_vertex = list(self.D_vertices)[0]

        # in visited we keep all the visited vertices from the current connected component
        visited = set()

        # we put the starting vertex as first item in queue
        visited.add(start_vertex)

        # in connected components we will keep graph objects containing dfs on each connected component
        connected_components = list()

        # nr_vertices_viseted - keeps count of how many vertices have been visited
        nr_vertices_visited = 0
        found_all_connected_components = False
        
        # all_viseted - keeps all vertices which already take part in a connected component
        all_visited = list()
        while found_all_connected_components == False:
            connected_component = self.dfs(start_vertex)
            for v in connected_component:
                all_visited.append(v)
                for n in list(self.D_vertices):
                    if n not in all_visited:
                        start_vertex = n
                        break
            
            # we create an auxiliary graph object
            auxiliary_graph = UndirectedGraph()
            for v in connected_component:
                auxiliary_graph.add_specific_vertex(v)
            for v in connected_component:
                for i in self.D_vertices[v]:
                    auxiliary_graph.addEdge(v,i)

            connected_components.append(auxiliary_graph)
            nr_vertices_visited += len(connected_component)
            if nr_vertices_visited == self.n:
                found_all_connected_components = True
            else:
                visited = set()
                visited.add(start_vertex)

        return connected_components

    def find_connencted_components_bfs(self):
        """
            finds all connected components
            return:
                connencted_components - (list) contains dictionaries of connected components
        """
        # first we choose the starting vertex
        start_vertex = list(self.D_vertices)[0]

        queue = list()
        distance = dict()
        visited = set()

        # we put the starting vertex as first item in queue
        queue.append(start_vertex)
        visited.add(start_vertex)
        distance[start_vertex] = 0
        connected_components = list()

        # vertices_viseted - keeps count of how many vertices have been visited
        nr_vertices_visited = 0
        found_all_connected_components = False
        # all_viseted - keeps all vertices which already take part in a connected component
        all_visited = list()
        while found_all_connected_components == False:
            while len(queue) != 0:
                x = queue.pop()
                for n in self.D_vertices[x]:
                    if n not in visited:
                        queue.append(n)
                        visited.add(n)
                        distance[n] = distance[x] + 1
            connected_components.append(visited)
            for v in visited:
                all_visited.append(v)
            nr_vertices_visited += len(distance)
            if nr_vertices_visited == self.n:
                found_all_connected_components = True
            else:
                for v in self.D_vertices.keys():
                    if v not in all_visited:
                        # we choose another starting vertex and so moving to another connected component
                        start_vertex = v
                        break
                queue = list()
                distance = dict()
                visited = set()
                queue.append(start_vertex)
                visited.add(start_vertex)
                distance[start_vertex] = 0

        return connected_components

### external functions ###  

def write_graph_external(graph, file_name):
    """
        writes the graph with the correspondig format in a file
        graph - the graph where the data is inserted (DictGraph)
        file_name - the name of the file (str)
    """
    f = open(file_name,"w")
    first_line = str(graph.n) + ' ' + str(graph.m) + '\n'
    f.write(first_line)
    lines = []
    for edge in graph.D_cost:
        line = str(edge[0]) + ' ' + str(edge[1]) + ' ' + str(graph.D_cost[edge]) + '\n'
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
    max_edges = int((no_vertices * (no_vertices - 1)) / 2)
    if no_edges >= max_edges:
            raise CompleteGraph

    graph = DictGraph()

    for i in range(no_vertices):
        graph.n += 1
        graph.D_in[i] = []
        graph.D_out[i] = []

    while graph.m != no_edges:
        v1 = random.randrange (0,no_vertices,1)
        v2 = random.randrange (0,no_vertices,1)
        cost = random.randrange (-9999,9999,1)
        if graph.isEdge(v1,v2) == False:
            graph.D_in[v1].append(v2)
            graph.D_out[v2].append(v1)
            graph.D_cost[(v1,v2)] = cost
            graph.m = len(graph.D_cost)

    return graph


###TESTS###