from graph_class import Graph
import sys

graph_file_path = sys.argv[1]

graph = Graph()
graph.read(graph_file_path)
table = graph.get_table()

def eulerianCheck():
  initial_vertice = None
  for vertice in range(len(table)):
    if graph.degree(vertice) > 0:
      initial_vertice = vertice + 1
      break
  if initial_vertice is None:
    print(0)
    return

  if table == []:
    print(0)
    return

  odd_counter = 0

  for vertice in range(len(table)):
    degree = graph.degree(vertice)

    if degree % 2 != 0:
      odd_counter += 1

  if odd_counter != 0:
    print(0)
    return

  stack = [initial_vertice]
  final_cycle = []

  neighbors_map = {}
  for v in range(1, len(table)+1):
    neighbors_map[v] = list(graph.get_neightbors(v))

  while stack != []:
    currentNode = stack[-1]

    if neighbors_map[currentNode]:
      neighbor = neighbors_map[currentNode].pop(0)
      neighbors_map[neighbor].remove(currentNode)

      stack.append(neighbor)
    else:
      # backtracking
      final_cycle.append(stack.pop())

  print(1)
  print(",".join(map(str, final_cycle)))

eulerianCheck()