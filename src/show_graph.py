def show_graph(graph):
    for v, neighbors in graph.items():
        print(f"{v} -> {neighbors}")
