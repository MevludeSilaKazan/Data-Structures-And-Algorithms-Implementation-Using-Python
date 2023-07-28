class Graph():

    def __init__(self):
        self.number_of_vertex = 0
        self.vertices = {}

    def add_vertex(self, data):
        if data not in self.vertices:
            self.vertices[data] = []
            self.number_of_vertex += 1

    def add_edge(self, source, target, weight=1):
        if target not in self.vertices[source]:
            self.vertices[source].append((target, weight))

    def show_connections(self):
        for vertex in self.vertices:
            connections = " ".join(f'{v}({w})' for v, w in self.vertices[vertex])
            total_weight = sum(w for _, w in self.vertices[vertex])
            print(f'{vertex} -->> {connections} (Total Weight: {total_weight})')


my_graph = Graph()
my_graph.add_vertex(10)
my_graph.add_vertex(11)
my_graph.add_vertex(12)
my_graph.add_edge(10, 11, 5)
my_graph.add_edge(10, 12, 7)
my_graph.add_edge(11, 12, 3)
my_graph.show_connections()

"""
10 -->> 11(5) 12(7) (Total Weight: 12)
11 -->> 12(3) (Total Weight: 3)
12 -->> (Total Weight: 0)
"""

print(my_graph.vertices)
# {10: [(11, 5), (12, 7)], 11: [(12, 3)], 12: []}

print(my_graph.number_of_vertex)
# 3
