from domain import DictGraph
from errors import CompleteGraph, AlreadyExists, EdgeNotFount


class UI:

    def __init__(self, file_name):
        self.graph = DictGraph()
        self.graph.read_file(file_name)

    def menu(self):
        print('-----------------------------')
        print('             MENU            |')
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
                v1 = int(input('first vertex: '))
                v2 = int(input('second vertex: '))
                try:
                    if self.graph.isEdge(v1, v2) == True:
                        print('There is an edge between the two vertices')
                    else:
                        print('No edge')
                except ValueError:
                    print('No edge')

            elif command == '4':
                v1 = int(input('give vertex: '))
                in_degree = self.graph.inDegree(v1)
                out_degree = self.graph.outDegree(v1)
                print('The in degree is: ', in_degree)
                print('The out degree is: ', out_degree)

            elif command == '5':
                v1 = int(input('give vertex: '))
                print(self.graph.outbound_edges(v1))

            elif command == '6':
                v1 = int(input('give vertex: '))
                print(self.graph.inbound_edges(v1))
            # elif command == '7':
            #     None

            elif command == '8.1':
                v1 = int(input('first vertex: '))
                v2 = int(input('second vertex: '))
                try:
                    print ('The cost is ', self.graph.get_cost(v1,v2))
                except EdgeNotFount:
                    print ("There is no such edge")
                except ValueError:
                    print ("At least one vertex does not exit")

            elif command == '8.2':
                v1 = int(input('first vertex: '))
                v2 = int(input('second vertex: '))
                new_cost = int(input('new cost: '))
                try:
                    self.graph.modify_cost(v1,v2,new_cost)
                except EdgeNotFount:
                    print ("There is no such edge")
                except ValueError:
                    print ("At least one vertex does not exit")

            elif command == '9.1':
                v1 = int(input('first vertex: '))
                v2 = int(input('second vertex: '))
                cost = int(input('new cost: '))
                try:
                    self.graph.addEdge(v1,v2,cost)
                except CompleteGraph:
                    print ("The graph is complete so no other edge can be added")
                except AlreadyExists:
                    print ("The edge already exists")

            elif command == '9.2':
                v1 = int(input('first vertex: '))
                v2 = int(input('second vertex: '))
                try:
                    self.graph.removeEdge(v1,v2)
                except ValueError:
                    print ("At least one vertex does not exit")
                except EdgeNotFount:
                    print ("no such edge")


            elif command == '9.3':
                self.graph.add_vertex()
            
            elif command == '9.4':
                v1 = int(input('give vertex: '))
                self.graph.remove_vertex(v1)
            
            elif command == '10':
                new_graph = DictGraph()
                try:
                    self.graph.copy_graph(new_graph)
                except ValueError:
                    print("missmatch oin object type")
            
            else:
                print ('Wrong command')