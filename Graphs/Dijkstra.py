from queue import PriorityQueue

class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)]
        self.visited = []

    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight
        self.edges[v][u] = weight


def dijkstra(graph, start_vertex):
    D = {v:float('inf') for v in range(graph.v)}
    D[start_vertex] = 0

    pq = PriorityQueue()
    pq.put((0, start_vertex))

    while not pq.empty():
        (dist, current_vertex) = pq.get()
        graph.visited.append(current_vertex)

        for neighbor in range(graph.v):
            if graph.edges[current_vertex][neighbor] != -1:
                distance = graph.edges[current_vertex][neighbor]
                if neighbor not in graph.visited:
                    old_cost = D[neighbor]
                    new_cost = D[current_vertex] + distance
                    if new_cost < old_cost:
                        pq.put((new_cost, neighbor))
                        D[neighbor] = new_cost
    return D


# a = 0
# b = 1
# c = 2
# d = 3
# e = 4
# f = 5
# g = 6
# h = 7
# i = 8

g = Graph(7)
g.add_edge(0, 1, 4) # a -> b
g.add_edge(0, 6, 7) # a -> g
g.add_edge(1, 2, 1) # b -> c
g.add_edge(1, 3, 2) # b -> d
g.add_edge(2, 0, 2) # c -> a
g.add_edge(2, 5, 6) # c -> f
g.add_edge(3, 2, 1) # d -> c
g.add_edge(3, 5, 4) # d -> f
g.add_edge(4, 2, 8) # e -> c
g.add_edge(5, 4, 1) # f -> e
g.add_edge(6, 4, 6) # g -> e
g.add_edge(6, 2, 4) # g -> c

# define starting vertex
start = 0
D = dijkstra(g, start)

for vertex in range(len(D)):
    print("Distance from vertex "+str(start)+" to vertex", vertex, "is", D[vertex])