from domain_GoianTudorGeorge_gr913_pw1 import DictGraph
from domain_GoianTudorGeorge_gr913_pw1 import UndirectedGraph
from domain_GoianTudorGeorge_gr913_pw1 import write_graph_external
from domain_GoianTudorGeorge_gr913_pw1 import create_random_graph

from errors_GoianTudorGeorge_gr913_pw1 import CompleteGraph, AlreadyExists, EdgeNotFount, NotExistentVertex

class UI:

    def __init__(self, file_name, file_name2):
        self.graph = DictGraph()
        self.graph.read_file(file_name)
        self.undirected_graph = UndirectedGraph()
        self.undirected_graph.read_file(file_name2)

    def menu(self):
        print('-----------------------------')
        print('             MENU            |')
        print('             Lab1            |')
        print('0. exit                      |')
        print('0.1 get data                 |')
        print('1. get number of vertices    |')
        print('2. parse vertices            |')
        print('3. check edge                |')
        print('4. in degree, out degree     |')
        print('5. parse outbound edges      |')
        print('6. parse inbound edges       |')
        # print('7. ends ov an edge')
        print('8.1. get cost                |')
        print('8.2. modify cost             |')
        print('9.1. add an edge             |')
        print('9.2. remove an edge          |')
        print('9.3. add a vertex            |')
        print('9.4 remove a vertex          |')
        print('10. copy the graph           |')
        print('11. writhe graph to a file   |')
        print('12. create a random graph    |')
        print('             Lab2            |')
        print('13. bfs forward              |')
        print('14. bfs backward             |')
        print('15. connencted using dfs     |')
        print('16. connencted using bfs     |')
        print('             Lab5            |')
        print('17. vertex cover             |')
        print('-----------------------------')


    def start(self):
        while True:
            self.menu()
            command = input('>')
            if command == '0':
                return
                
            elif command == '0.1':
                print(self.graph.n)
                print(self.graph.m)
                print(self.graph.D_out)
                print(self.graph.D_in)
                print(self.graph.D_cost)

            elif command == '1':
                print('The number of vertices is ', self.graph.nrVertices())

            elif command == '2':
                print('The itterable list of vertices is ', self.graph.vertices())

            elif command == '3':
                try:
                    v1 = int(input('first vertex: '))
                    v2 = int(input('second vertex: '))
                    try:
                        if self.graph.isEdge(v1, v2) == True:
                            print('There is an edge between the two vertices')
                        else:
                            print('No edge')
                    except ValueError:
                        print('No edge')
                except ValueError:
                    print("bad input!!")
                

            elif command == '4':
                try:
                    v1 = int(input('give vertex: '))
                    in_degree = self.graph.inDegree(v1)
                    out_degree = self.graph.outDegree(v1)
                    print('The in degree is: ', in_degree)
                    print('The out degree is: ', out_degree)
                except ValueError:
                    print("bad input!!")

            elif command == '5':
                try:
                    v1 = int(input('give vertex: '))
                    print(self.graph.outbound_edges(v1))
                except ValueError:
                    print("bad input!!")

            elif command == '6':
                try:
                    v1 = int(input('give vertex: '))
                    print(self.graph.inbound_edges(v1))
                except ValueError:
                    print("bad input!!")

            elif command == '8.1':
                try:
                    v1 = int(input('first vertex: '))
                    v2 = int(input('second vertex: '))
                    try:
                        print ('The cost is ', self.graph.get_cost(v1,v2))
                    except EdgeNotFount:
                        print ("There is no such edge")
                    except ValueError:
                        print ("At least one vertex does not exit")
                except ValueError:
                    print("bad input!!")

            elif command == '8.2':
                try:  
                    v1 = int(input('first vertex: '))
                    v2 = int(input('second vertex: '))
                    new_cost = int(input('new cost: '))
                    try:
                        self.graph.modify_cost(v1,v2,new_cost)
                    except EdgeNotFount:
                        print ("There is no such edge")
                    except ValueError:
                        print ("At least one vertex does not exit")
                except ValueError:
                    print("bad input!!")

            elif command == '9.1':
                try:
                    v1 = int(input('first vertex: '))
                    v2 = int(input('second vertex: '))
                    cost = int(input('new cost: '))
                    try:
                        self.graph.addEdge(v1,v2,cost)
                    except CompleteGraph:
                        print ("The graph is complete so no other edge can be added")
                    except AlreadyExists:
                        print ("The edge already exists")
                except ValueError:
                    print("bad input!!")

            elif command == '9.2':
                try:
                    v1 = int(input('first vertex: '))
                    v2 = int(input('second vertex: '))
                    try:
                        self.graph.removeEdge(v1,v2)
                    except ValueError:
                        print ("At least one vertex does not exit")
                    except EdgeNotFount:
                        print ("no such edge")
                except ValueError:
                    print("bad input!!")                        


            elif command == '9.3':
                self.graph.add_vertex()
            
            elif command == '9.4':
                try:
                    v1 = int(input('give vertex: '))
                    self.graph.remove_vertex(v1)
                except ValueError:
                    print("bad input!!")            

            elif command == '10':
                new_graph = DictGraph()
                try:
                    self.graph.copy_graph(new_graph)
                except ValueError:
                    print("missmatch oin object type")

            elif command == '11':
                file_name = input('give file name: ')
                write_graph_external(self.graph, file_name)
            
            elif command == '12':
                try:
                    n = int(input('give number of vertices: '))
                    m = int(input('give number of edges: '))
                    try:
                        self.graph = create_random_graph(n,m)
                    except CompleteGraph:
                        print('There are too many edges for the amount of vertices')         
                except ValueError:
                    print("bad input!!")           
            
            elif command == '13':
                try:
                    v1 = int(input('give start vertex: '))
                    v2 = int(input('give end vertex: '))
                    try:
                        print("the minimum path lenght is " + str(self.graph.bfs_forward(v1,v2)))      
                    except NotExistentVertex:
                        print("at least one vertex does not exist")
                except ValueError:
                    print("bad input!!") 
            
            elif command == '14':
                try:
                    v1 = int(input('give start vertex: '))
                    v2 = int(input('give end vertex: '))
                    try:
                        print("the minimum path lenght is " + str(self.graph.bfs_forward(v1,v2)))      
                    except NotExistentVertex:
                        print("at least one vertex does not exist")
                except ValueError:
                    print("bad input!!") 
            
            elif  command == '15':
                connected_components = self.undirected_graph.find_connencted_components_dfs()
                for i in range (0,len(connected_components)):
                    print ("connected component " + str(i+1) + " : " + str(connected_components[i]))

            elif command == '16':
                connected_components = self.undirected_graph.find_connencted_components_bfs()
                for i in range (0,len(connected_components)):
                    print ("connected component " + str(i+1) + " -> " + str(list(connected_components[i])))
            
            elif command == '17':
                vc = self.undirected_graph.vertex_cover() 
                
                vca = self.undirected_graph.vertex_cover_aproximation()
                
                print("vertex cover without aproximation: ")
                print(vc)

                print("vertex cover with aproximation: ")
                print(vca)

            else:
                print ('Wrong command')