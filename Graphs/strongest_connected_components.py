# Kosaraju's algorithm to find strongly connected components in Python


from collections import defaultdict

class Graph:

    def __init__(self, vertex):
        self.V = vertex
        self.graph = defaultdict(list)

    # Add edge into the graph
    def add_edge(self, s, d):
        self.graph[s].append(d)

    # dfs
    def dfs(self, d, visited_vertex):
        visited_vertex[d] = True
        print(d, end='')
        for i in self.graph[d]:
            if not visited_vertex[i]:
                self.dfs(i, visited_vertex)

    def fill_order(self, d, visited_vertex, stack):
        visited_vertex[d] = True
        for i in self.graph[d]:
            if not visited_vertex[i]:
                self.fill_order(i, visited_vertex, stack)
        stack = stack.append(d)

    # transpose the matrix
    def transpose(self):
        g = Graph(self.V)

        for i in self.graph:
            for j in self.graph[i]:
                g.add_edge(j, i)
        return g

    # Print stongly connected components
    def print_scc(self):
        stack = []
        visited_vertex = [False] * (self.V)

        for i in range(self.V):
            if not visited_vertex[i]:
                self.fill_order(i, visited_vertex, stack)

        gr = self.transpose()

        visited_vertex = [False] * (self.V)

        while stack:
            i = stack.pop()
            if not visited_vertex[i]:
                gr.dfs(i, visited_vertex)
                print("")
            

# a = 0
# b = 1
# c = 2
# d = 3
# e = 4
# f = 5
# g = 6
# h = 7
# i = 8

g = Graph(9)
g.add_edge(0, 1) # a -> b
g.add_edge(0, 3) # a -> d
g.add_edge(1, 2) # b -> c
g.add_edge(1, 3) # b -> d
g.add_edge(2, 4) # c -> e
g.add_edge(4, 1) # e -> b
g.add_edge(3, 4) # d -> e
g.add_edge(4, 5) # e -> f
g.add_edge(5, 2) # f -> c
g.add_edge(5, 7) # f -> h
g.add_edge(7, 4) # h -> e
g.add_edge(7, 8) # h -> i
g.add_edge(5, 8) # f -> i
g.add_edge(6, 7) # g -> h
g.add_edge(6, 3) # g -> d


print("Strongly Connected Components:")
g.print_scc()