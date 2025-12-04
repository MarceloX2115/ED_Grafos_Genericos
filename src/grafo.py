class Grafo:
    def __init__(self):
        self.adj = {}

    def add_vertex(self, v):
        if v not in self.adj:
            self.adj[v] = []

    def remove_vertex(self, v):
        if v in self.adj:
            self.adj.pop(v)
            for neighbors in self.adj.values():
                if v in neighbors:
                    neighbors.remove(v)

    def add_edge(self, v1, v2):
        if v1 in self.adj and v2 in self.adj:
            if v2 not in self.adj[v1]:
                self.adj[v1].append(v2)
            if v1 not in self.adj[v2]:
                self.adj[v2].append(v1)

    def remove_edge(self, v1, v2):
        if v1 in self.adj and v2 in self.adj:
            if v2 in self.adj[v1]:
                self.adj[v1].remove(v2)
            if v1 in self.adj[v2]:
                self.adj[v2].remove(v1)

    def show(self):
        return {v: list(neighbors) for v, neighbors in self.adj.items()}

    def show_pretty(self):
        lines = []
        for v, neighbors in self.adj.items():
            lines.append(f"{v} -> {', '.join(neighbors)}")
        return "\n".join(lines)
