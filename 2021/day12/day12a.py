from aocd import data
import networkx as nx

""" with open("input.txt") as f:
    data = f.read() """

data = data.splitlines()
g = nx.Graph()
g.nodes.data("big", default=False)
paths = []


def findPath(node, path: list):
    my_path = path.copy()
    my_path.append(node)
    if node == "end":
        paths.append(my_path)
        return
    for n in nx.neighbors(g, node):
        if (n.islower() and n not in my_path) or n.isupper():
            findPath(n, my_path)


for line in data:
    a, b = line.split("-")
    g.add_edge(a, b)
    if a.isupper():
        g.nodes[a]["big"] = True
    if b.isupper():
        g.nodes[b]["big"] = True
print("# of edges: {}".format(g.number_of_edges()))
print("# of nodes: {}".format(g.number_of_nodes()))

findPath("start", [])
print(paths)
print(len(paths))
