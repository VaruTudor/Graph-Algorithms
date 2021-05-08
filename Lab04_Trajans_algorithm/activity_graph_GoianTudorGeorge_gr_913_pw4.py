class isDAG(Exception):
    pass


class Activity:
    def __init__(self, name, duration, prequisites_list = []):
        self.name = name
        self.duration = duration
        self.prequisites_list = prequisites_list

        self.earliest_begin_time = 0
        self.earliest_end_time = 0
        self.latest_begin_time = 0
        self.latest_end_time = 0
    
    def __str__(self):
        s = "| " + str(self.earliest_begin_time) + " " + self.name + " " + str(self.earliest_end_time) + " |\n"
        s +=  "| " + str(self.latest_begin_time) + " " + str(self.duration)  + " " + str(self.latest_end_time) + " |\n"
        s += "preq:"
        if len(self.prequisites_list) > 0:
            s += " ("
            for a in self.prequisites_list:
                s += a 
                s += ", "
            s = s[:-2]
            s += ")\n"
        else:
            s += "\n" 
        return s
    
    def __repr__(self):
        s = "|| " + str(self.earliest_begin_time) + " " + self.name + " " + str(self.earliest_end_time) + " | " + str(self.latest_begin_time) + " " + str(self.duration)  + " " + str(self.latest_end_time) + " ||" 
        return s

class DictGraph:
    
    def __init__(self):
        """
            Creates a graph using dictionaries
        """
        self.n = 0  # the number of vertices
        self.m = 0  # the number of edges
        self.D_out = {} 
        self.D_in = {}  
        self.D_cost = {} 
        self.activities = []
        self.topological_order = []

    def __str__(self):
        s = "\nVERTICES: \n"
        n = "\nEDGES: \n"
        for v in self.D_out:
            s += str(v)
            for k in self.D_out[v]:
                n += "( "+ repr(v) + " -> " + repr(k) + " ) \n"

        s += n
        return s
        
    def print_activities(self):
        for a in self.activities:
            print(str(a))

    def read_file(self, file_name):
        """
            Reads a graph from a file
            file_name - the name of the file (string)
        """
        f = open(file_name,'r')
        self.activities.append( Activity("X", 0) )

        while True:
            line = f.readline()
            if len(line) == 0:
                break
            line = line[:-1]
            line = line.split(' ')

            if len(line) == 2:
                self.activities.append(Activity(line[0], int(line[1]), [] ))

            elif len(line) == 3:
                new_activity = Activity(line[0], int(line[1]), [] )
                preq = line[2].split(',')
                for a in preq:
                    new_activity.prequisites_list.append(a)
                self.activities.append(new_activity)

        self.activities.append( Activity("Y", 0) )

    
    def find_activity_by_name(self, name):
        for a in self.activities:
            if a.name == name:
                return a
    
    def find_index_of_activity_by_name(self, name):
        index = 0
        for a in self.activities:
            if a.name == name:
                return index
            index += 1

    def init_with_activities(self):

        self.n = len(self.activities)
        for a in self.activities:
            self.D_in[a] = []
            self.D_out[a] = []
        for a in self.activities:
            # self.D_out[a] = []
            # self.D_in[a] = []
            if len(a.prequisites_list) == 0: 
                if a.name != "X" and a.name != "Y":
                    self.D_out[ self.find_activity_by_name("X") ].append(a)
                    self.D_in[a].append( self.find_activity_by_name("X") )
            else:
                for pa in a.prequisites_list:
                        self.D_in[a].append( self.find_activity_by_name(pa) )
                        self.D_out[ self.find_activity_by_name(pa) ].append(a)
        
        for a in self.activities:
            if self.D_out[a] == [] and a.name != "Y":
                self.D_out[a].append( self.find_activity_by_name("Y") )
                self.D_in[ self.find_activity_by_name("Y") ].append(a)

    def total_time(self):
        a = self.find_activity_by_name("X").earliest_begin_time
        b = self.find_activity_by_name("Y").latest_end_time
        return b-a

    ### TRAJAN ###

    def Trajan(self):
        topological_list = list()
        visited = list()
        recursion_stack = list()
        # DAF = True
        for _ in range(self.n + 1):
            visited.append(False)
            # recursion_stack.append(False)
        while len(topological_list) != self.n:
            for v in list(self.D_in):
                if visited[self.find_index_of_activity_by_name(v.name)] == False:
                    start_vertex = v
                    recursion_stack.append( self.find_index_of_activity_by_name(v.name) )
                    break
            self.visit(start_vertex, visited, topological_list, recursion_stack)
        topological_list.reverse()
        return topological_list

    def visit(self, vertex, visited, topological_list, recursion_stack):
        """
            Help function for Trajan's DFS alogorithm
        """
        recursion_stack.append( self.find_index_of_activity_by_name(vertex.name) )
        if visited[ self.find_index_of_activity_by_name(vertex.name) ] == False:
            for neighbor in self.D_out[vertex]:
                if self.find_index_of_activity_by_name(neighbor.name) in recursion_stack:
                    # raise isDAG
                    None
                self.visit(neighbor, visited, topological_list, recursion_stack)
            visited[ self.find_index_of_activity_by_name(vertex.name) ] = True
            topological_list.append(vertex)
            recursion_stack.remove( self.find_index_of_activity_by_name(vertex.name) )
        
    def set_times(self, file_name):
        self.read_file(file_name)
        self.init_with_activities()
        tp_order = self.Trajan()
        self.topological_order = tp_order

        for a in tp_order:
            if a.name == "X":
                a.earliest_begin_time = a.earliest_end_time = 0
            else:
                maximum = 0
                for i in self.D_in[a]:
                    if i.earliest_end_time > maximum:
                        maximum = i.earliest_end_time
                a.earliest_begin_time = maximum
                a.earliest_end_time = a.earliest_begin_time + a.duration
         
        tp_order.reverse()
        for a in tp_order:
            if a.name == "Y":
                a.latest_end_time = a.earliest_end_time
                a.latest_begin_time = a.latest_end_time - a.duration
            else:
                minimum = 1000000
                for i in self.D_out[a]:
                    if i.latest_begin_time < minimum:
                        minimum = i.latest_begin_time
                a.latest_end_time = minimum
                a.latest_begin_time = a.latest_end_time - a.duration