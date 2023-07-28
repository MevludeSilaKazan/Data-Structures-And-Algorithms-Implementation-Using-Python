class Graph():
    def __init__(self):
        self.number_of_nodes = 0
        self.adjacency_list = {}

    def insert_node(self, data):
        if data not in self.adjacency_list:
            self.adjacency_list[data] = []
            self.number_of_nodes += 1

    def insert_edge(self, vertex1, vertex2):
        if vertex2 not in self.adjacency_list[vertex1]:
            self.adjacency_list[vertex1].append(vertex2)

    def show_connections(self):
        for node in self.adjacency_list:
            print(f'{node} -->> {" ".join(map(str, self.adjacency_list[node]))}')


my_graph = Graph()
my_graph.insert_node(1)
my_graph.insert_node(2)
my_graph.insert_node(3)
my_graph.insert_edge(1, 2)
my_graph.insert_edge(1, 3)
my_graph.insert_edge(2, 3)
my_graph.show_connections()

print(my_graph.adjacency_list)


print(my_graph.number_of_nodes)

