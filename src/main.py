from grafo import Grafo
from show_graph import show_graph

g = Grafo()
g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'C')

print('Lista de adjacência (raw):')
print(g.show())

print('\nLista de adjacência (formatada):')
print(g.show_pretty())

print('\nImpressão demonstrativa:')
show_graph(g.show())
