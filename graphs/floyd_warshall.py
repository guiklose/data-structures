from graph_class import Graph
import sys

graph_file_path = sys.argv[1]

graph = Graph()
graph.read(graph_file_path)
table = graph.get_table()

# printer
def print_floyd_warshall(distances):
  for i in range(len(table)):
    row = []
    for j in range(len(table)):
      if distances[i][j] == float('inf'):
        row.append("inf")
      else:
        row.append(str(distances[i][j]))
    print(f"{i+1}:{','.join(row)}")

def floyd_warshall():
  distances = []

  # Populate distance matrix
  for _ in range(len(table)):
    distances.append([float('inf')] * len(table))

  for i in range(len(table)):
    for j in range(len(table)):
      if i == j:
        distances[i][j] = 0
      elif table[i][j] != -1:
        distances[i][j] = table[i][j]

  # floydwarshall
  for k in range(len(table)):
    for i in range(len(table)):
      for j in range(len(table)):
        if distances[i][k] + distances[k][j] < distances[i][j]:
          distances[i][j] = distances[i][k] + distances[k][j]

  print_floyd_warshall(distances)

floyd_warshall()