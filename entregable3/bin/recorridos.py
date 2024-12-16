from typing import Dict, List, Optional, Tuple, Set

class Graph:
    """Representación de un grafo no dirigido para poder usar con el recorrido en profundidad."""
    def __init__(self):
        self.adjacency_list: Dict[str, Set[str]] = {}

    def add_vertex(self, vertex: str):
        """Añadir un vértice al grafo si no existe."""
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = set()

    def add_edge(self, source: str, target: str):
        """Añadir una arista entre los vértices source y target."""
        self.add_vertex(source)
        self.add_vertex(target)
        self.adjacency_list[source].add(target)
        self.adjacency_list[target].add(source)

    def get_neighbors(self, vertex: str) -> Set[str]:
        """Devuelve los vecinos de un vértice."""
        return self.adjacency_list.get(vertex, set())

class Recorrido:
    """Clase base para recorrer un grafo."""
    def __init__(self, grafo: Graph):
        self._grafo = grafo
        self._tree: Dict[str, Tuple[Optional[str], float]] = {}  # Árbol de recorrido
        self._path: List[str] = []  # Camino recorrido
        self._visited: Set[str] = set()  # Conjunto de vértices visitados

    def path_to_origin(self, vertex: str) -> List[str]:
        """Construye el camino hacia el origen desde el vértice dado."""
        path = []
        current = vertex
        while current is not None:
            path.append(current)
            current = self._tree.get(current, (None, 0))[0]  # Sigue el predecesor
        return path[::-1]  # Regresa el camino desde el origen al vértice dado

    def origin(self, vertex: str) -> str:
        """Determina el origen del recorrido a partir de un vértice dado."""
        while self._tree.get(vertex, (None, 0))[0] is not None:
            vertex = self._tree[vertex][0]  # Sigue los predecesores
        return vertex

    def groups(self) -> Dict[str, Set[str]]:
        """Organiza los vértices en grupos basados en su origen."""
        groups = {}
        for vertex, (predecessor, _) in self._tree.items():
            if predecessor not in groups:
                groups[predecessor] = set()
            groups[predecessor].add(vertex)
        return groups

class RecorridoEnProfundidad(Recorrido):
    """Implementación de un recorrido en profundidad (DFS)."""
    def __init__(self, grafo: Graph):
        super().__init__(grafo)

    @classmethod
    def of(cls, grafo: Graph):
        """Método de factoría para crear una nueva instancia de RecorridoEnProfundidad."""
        return cls(grafo)

    def traverse(self, source: str):
        """Realiza un recorrido en profundidad (DFS) comenzando desde el vértice source."""
        self._tree = {}  # Reinicia el árbol de recorrido
        self._path = []  # Reinicia el camino recorrido
        self._visited = set()  # Reinicia los vértices visitados
        self._dfs(source, None, 0)

    def _dfs(self, vertex: str, predecessor: Optional[str], cost: float):
        """Método auxiliar para realizar el DFS de manera recursiva."""
        if vertex in self._visited:
            return
        self._visited.add(vertex)
        self._tree[vertex] = (predecessor, cost)  # Guarda el predecesor y el costo
        self._path.append(vertex)  # Añade el vértice al recorrido
        for neighbor in self._grafo.get_neighbors(vertex):
            if neighbor not in self._visited:
                self._dfs(neighbor, vertex, cost + 1)  # Se asume un peso de 1 por arista