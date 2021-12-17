from collections import defaultdict
import networkx as nx

with open("input.txt") as f:
    data = f.read()
data = data.splitlines()
data = [[int(x) for x in line] for line in data]
g = nx.grid_graph([len(data), len(data[0])])
nx.set_edge_attributes(g, {e: data[e[0][1]][e[0][0]] for e in g.edges()}, "cost")


def cost(a, b, d):
    return data[a[0]][a[1]]


# print(nx.astar_path(g, (0, 0), (len(data) - 1, len(data[0]) - 1), weight="cost"))
print(
    nx.astar_path_length(g, (0, 0), (len(data) - 1, len(data[0]) - 1), weight="cost")
    + data[-1][-1]
)
