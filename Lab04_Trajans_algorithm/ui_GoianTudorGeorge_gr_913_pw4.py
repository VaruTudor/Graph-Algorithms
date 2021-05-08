from activity_graph_GoianTudorGeorge_gr_913_pw4 import Activity, DictGraph

class UI:

    def __init__(self, file_name):
        self.__DAG = 0
        self.graph = DictGraph()
        try:
            self.graph.set_times(file_name)
        except RecursionError:
            self.__DAG = 1
            print ("graph is not a DAG")

    def print_menu(self):
        print ("--------------------------------------------")
        print ("|                  MENU                    |")
        print ("| 0. exit                                  |")
        print ("| 1. topological order                     |")
        print ("| 2. times for activities + project time   |")
        print ("| 3. critical activities                   |")
        print ("| 4. print the graph                       |")
        print ("--------------------------------------------")

    def print_trojan(self):
        # print ( list(reversed(self.graph.topological_order)) )
        for a in  list(reversed(self.graph.topological_order)):
            print(a)
        
        print ("\n")

    def print_earliest_latest(self):
        for a in self.graph.activities:
            s = str(a.name) + " - earliest start: " + str(a.earliest_begin_time) + ", latest start: " + str(a.latest_begin_time)
            print(s) 
        total_time = self.graph.total_time()
        print ("total time of project is " + str(total_time))

    def print_critical_activities(self):
        for a in self.graph.activities:
            if (a.earliest_begin_time == a.latest_begin_time):
                print(str(a))

    def run(self):
        if self.__DAG == 0:
            while(True):
                self.print_menu()
                command = input("> ")

                if command == '1':
                    self.print_trojan()
                elif command == '0':
                    return
                elif command == '2':
                    self.print_earliest_latest()
                elif command == '3':
                    self.print_critical_activities()
                elif command == '4':
                    print(str(self.graph))
                else:
                    print ("wrong command")

