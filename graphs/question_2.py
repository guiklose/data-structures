from graph_class import Graph

graph = Graph()

graph.ler('test.txt')

# grau = graph.grau(4)

# print('grau: ', grau)

# haAresta = graph.haAresta(3, 2)

# print('haAresta: ', haAresta)

# vizinhos = graph.vizinhos(1)

# print('vizinhos: ', vizinhos)

# peso = graph.peso(4, 1)

# print('peso: ', peso)

# print('qtdVertices: ', graph.qtdVertices())
# print('qtdArestas: ', graph.qtdArestas())

table = graph.get_table()

print(table)

queue = []

def busca_largura(vertice):
  for vertice in table[vertice - 1]:
