class Graph():

    def __init__(self):
        self.number_of_vertex = 0
        self.vertices = {}

    def add_vertex(self, data):

        if data not in self.vertices:
            self.vertices[data] = []
            self.number_of_vertex += 1
            return
        
    def add_edge(self, source, target):
        if target not in self.vertices[source]:
            self.vertices[source].append(target)
            self.vertices[target].append(source)

           
            return
        return "Edge already exists"

#Finally we will implement a custom print method which willl print the nodes and their connections
    def show_connections(self):
        for vertex in self.vertices:
            print(f'{vertex} -->> {" ".join(map(str, self.vertices[vertex]))}')


my_graph = Graph()
my_graph.add_vertex(10)
my_graph.add_vertex(11)
my_graph.add_vertex(12)
my_graph.add_edge(10,11)
my_graph.add_edge(10,12)
my_graph.add_edge(11,12)
my_graph.show_connections()


print(my_graph.vertices)


print(my_graph.number_of_vertex)
