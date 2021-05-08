@ Goian Tudor George, IE1, gr913

The graph was represented using three dictionaries 
(D_out - keys: vertices - values: outbound vertices
 D_in - keys: vertices - values: inbound vertices
 D_cost - keys: tuples consisting in both ends of an edge - values: the 'cost' (=the integer attached to that edge))
Methods used:
1.read_file(self, file_name)
the method reads a graph from a file respecting the required format

2.remove_vertex(self, x)
removes a vertex form the graph
( removes it from all three dictionaries )

3.get_cost(self, x, y)
returns the cost of the edge starting from x and ending in y
( uses D_cost )
*raises ValueError if one of the vertices does not exit
*raises EdgeNotFound if the edge does not exist

4.modify_cost(self, x, y, new_cost)
modifies the cost of the edge starting from x and ending in y
*raises ValueError if one of the vertices does not exit
*raises EdgeNotFound if the edge does not exist

5.isEdge(self, x, y)
returns if there exists an edge between x and y
*raises ValueError if one of the vertices does not exit

6.inDegree(self, x)
returns the in-degree of an edge
*raises ValueError if the vertex does not exit

7.outDegree(self, x)
returns the out-degree of an edge
*raises ValueError if the vertex does not exit

8.addEdge(self, x, y, cost)
adds an edge to the grph
*raises CompleteGraph if the graph is complete
*raises AlreadyExists if the edge is already in the graph

9.removeEdge
removes the edge starting from x and ending in y
*raises ValueError if one of the vertices does not exit
*raises EdgeNotFound if the edge does not exist

10.add_vertex(self)
adds a vertex to the graph
(appends it to both D_in and D_out as a key)

11.nrVertices(self)
returns the number of verices form the graph

12.vertices(self)
returns a list containing all the vertices

13.copy_graph(self,new_graph)
copies the graph
*returns ValueError if the parameter is not a graph object

### external functions ###

14.write_graph_external(graph, file_name)
writes the graph to a file

15.read_graph_external(graph, filename)
reads the graph from a file

16.create_random_graph(no_vertices, no_edges)
creates and return a random graph

# The program was implemented using Python 3

	