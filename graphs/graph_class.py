class Graph:
  def __init__(self):
    self.__qtd_vertices = 0
    self.__qtd_arestas = 0
    self.__table = []
    self.__rotulos = []

  def get_table(self):
    return self.__table

  # O(1) - Assegurado por atributo extra '__qtd_vertices'
  def qtdVertices(self):
    return self.__qtd_vertices

  # O(1) - Assegurado por atributo extra '__qtd_arestas'
  def qtdArestas(self):
    return self.__qtd_arestas

  # O(n) n sendo a quantidade de vertices.
  def grau(self, v):
    quantity_vertices = 0
    for element in self.__table[v - 1]:
      if (element):
        quantity_vertices += 1
    return quantity_vertices

  # O(n) n sendo a quantidade de vertices.
  def vizinhos(self, v):
    vizinhos = []
    index = 0

    for vertice in self.__table[v - 1]:
      index += 1

      if vertice != float('inf'):
        vizinhos.append(index)

    return vizinhos

  # O(1)
  def haAresta(self, u, v):
    if (self.__table[u - 1][v - 1]):
      return True
    return False

  # O(1)
  def peso(self, u, v):
    return self.__table[u - 1][v - 1]

  # O(n) - Depende do número de linhas de entrada.
  def ler(self, arquivo):
    file = open(arquivo, 'r', encoding='utf-8')

    content = file.readlines()

    # Get vertices length
    len_vertice = int(content.pop(0).split()[1])

    # '+1' é para se livrar do '*edges'
    for i in range(len_vertice + 1):
      vertice_info = content.pop(0).split()

      if vertice_info[0] == '*edges':
        break

      # Populando numero de linhas da tabela a.k.a vertices
      self.__table.append([])
      # Salvando em estrutura separada os rotulos
      self.__rotulos.append((vertice_info[1], self.qtdVertices()))
      # Atualizando info da quantidade de vertices
      self.__qtd_vertices += 1

      for i in range(len_vertice):
        self.__table[self.qtdVertices() - 1].append(float('inf'))

    # Populando o Grafo com valores de arestas
    for l in range(len(content)):
      aresta_info = content.pop(0).split()
      aresta_start = int(aresta_info[0])
      aresta_final = int(aresta_info[1])

      self.__table[aresta_start - 1][aresta_final - 1] = int(aresta_info[2])
      # Grafos não dirigidos tem relação mutua.
      self.__table[aresta_final - 1][aresta_start - 1] = int(aresta_info[2])

      # Atualizando info da quantidade de arestas
      self.__qtd_arestas += 1
