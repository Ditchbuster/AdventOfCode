from collections import defaultdict
import networkx as nx


def cost(a):
    y = a[0]
    x = a[1]
    modx = x % len(data)
    mody = y % len(data)
    r = data[mody][modx] + int(y / len(data)) + int(x / len(data))
    r = r % 10 + int(r / 10)
    return r


with open("input.txt") as f:
    data = f.read()
data = data.splitlines()
data = [[int(x) for x in line] for line in data]
g = nx.grid_graph([len(data) * 5, len(data[0]) * 5])
nx.set_edge_attributes(g, {e: cost((e[1][0], e[1][1])) for e in g.edges()}, "cost")

# nx.astar_path(g, (0, 0), (len(data) * 5 - 1, len(data) * 5 - 1), weight="cost")
""" path = nx.dijkstra_path(
    g, (0, 0), (len(data) * 5 - 1, len(data) * 5 - 1), weight="cost"
) """
print(
    nx.dijkstra_path_length(
        g, (0, 0), (len(data) * 5 - 1, len(data) * 5 - 1), weight="cost"
    )
)
""" print(path)
print("".join([str(cost(x)) for x in path]))
for y in range(len(data) * 5):
    print("".join([str(cost((y, x))) for x in range(len(data) * 5)]))
 """
