from graph_class import Graph
import sys
import heapq

graph_file_path = sys.argv[1]
initial_vertice = int(sys.argv[2])

graph = Graph()
graph.read(graph_file_path)
table = graph.get_table()

heap = []
visited_nodes = {}

def print_dijkstra(visited_nodes):
  for v in sorted(visited_nodes.keys()):
    node = visited_nodes[v]
    if node["dist"] == float("inf"):
      path_str = ""
    else:
      path_str = ",".join(map(str, node["path"]))
    print(f"{v}: {path_str}; d={node['dist']}")

def dijkstra(initial_vertice):
  if table == []:
    return print_dijkstra([])

  heapq.heappush(heap, (0, initial_vertice))

  for vertice in range(1, len(table) + 1):
    visited_nodes[vertice] = {"dist": float("inf"), "path": []}

  visited_nodes[initial_vertice]["dist"] = 0
  visited_nodes[initial_vertice]["path"] = [initial_vertice]

  while heap != []:
    current_dist, vertice = heapq.heappop(heap)

    if current_dist > visited_nodes[vertice]["dist"]:
      continue

    neighbors = graph.get_neightbors(vertice)
    for index in neighbors:
      new_weight = graph.weight(vertice, index) + current_dist

      if (visited_nodes[index]["dist"] > new_weight):
        visited_nodes[index]["dist"] = new_weight
        visited_nodes[index]["path"] = visited_nodes[vertice]["path"] + [index]
        heapq.heappush(heap, (new_weight, index))

  print_dijkstra(visited_nodes)

dijkstra(initial_vertice)