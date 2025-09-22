from graph_class import Graph
import sys

graph_file_path = sys.argv[1]
initial_vertice = int(sys.argv[2])

graph = Graph()
graph.read(graph_file_path)
table = graph.get_table()

queue = []
visited_nodes = []

def printBFS(visited_nodes):
  distances = {}
  for node in visited_nodes:
    d = node['distance']
    v = node['vertice']

    if d not in distances:
      distances[d] = []

    distances[d].append(v)

  for dist in sorted(distances):
    print(str(dist) + ": " + ",".join(str(x) for x in sorted(distances[dist])))


def BFS(initial_vertice):
  if table == []:
    return printBFS([])

  queue.append({ "vertice": initial_vertice, "distance": 0 })

  while queue != []:
    currentNode = queue.pop(0)

    if any(node["vertice"] == currentNode["vertice"] for node in visited_nodes):
      continue

    visited_nodes.append(currentNode)

    neighbors = graph.get_neightbors(int(currentNode["vertice"]))
    for index in neighbors:
      queue.append({ "vertice": index, "distance": currentNode["distance"] + 1 })

  printBFS(visited_nodes)

BFS(initial_vertice)