class Graph:
  def __init__(self):
    self.__vertice_count = 0
    self.__edge_count = 0
    self.__table = []
    self.__labels = []

  def get_table(self):
    return self.__table

  # O(1)
  def vertice_count(self):
    return self.__vertice_count

  # O(1)
  def edge_count(self):
    return self.__edge_count

  # O(n)
  def degree(self, v):
    if v == float("inf"):
      return 0

    quantity_vertices = 0
    for element in self.__table[v - 1]:
      if (element != float("inf")):
        quantity_vertices += 1
    return quantity_vertices

  # O(n)
  def get_neightbors(self, v):
    vizinhos = []
    index = 0

    for vertice in self.__table[v - 1]:
      index += 1

      if vertice != float("inf"):
        vizinhos.append(index)

    return vizinhos

  # O(1)
  def has_edge(self, u, v):
    return self.__table[u - 1][v - 1] != float("inf")

  # O(1)
  def weight(self, u, v):
    return self.__table[u - 1][v - 1]

  # O(n)
  def read(self, path):
    file = open(path, "r", encoding="utf-8")

    content = file.readlines()

    len_vertice = int(content.pop(0).split()[1])

    for i in range(len_vertice + 1):
      vertice_info = content.pop(0).split()

      if vertice_info[0] == "*edges":
        break

      self.__table.append([])
      self.__labels.append((vertice_info[1], self.vertice_count()))
      self.__vertice_count += 1

      for i in range(len_vertice):
        self.__table[self.vertice_count() - 1].append(float("inf"))

    for l in range(len(content)):
      edge_info = content.pop(0).split()

      if edge_info:
        start_edge = int(edge_info[0])
        final_edge = int(edge_info[1])

        self.__table[start_edge - 1][final_edge - 1] = float(edge_info[2])
        self.__table[final_edge - 1][start_edge - 1] = float(edge_info[2])

        self.__edge_count += 1
    else:
      if self.__edge_count == 0:
        self.__table = []
