class Graph:
    def __init__(self, directed=False):
        """Inicializa el grafo. Si 'directed' es True, el grafo será dirigido."""
        self.directed = directed  # Tipo de grafo (dirigido o no dirigido)
        self.vertices = set()  # Conjunto de vértices
        self.edges = {}  # Diccionario de aristas {origen: {destino: peso}}
        self.predecessors = {}  # Diccionario de predecesores {vértice: set de predecesores}
        self.successors = {}  # Diccionario de sucesores {vértice: set de sucesores}
        self._weight = {}  # Diccionario de pesos de las aristas {(origen, destino): peso}

    def __add_neighbors(self, vertex, neighbor):
        """Añade un vecino al conjunto de vecinos de un vértice."""
        if vertex not in self.successors:
            self.successors[vertex] = set()
        self.successors[vertex].add(neighbor)

    def __add_predecessors(self, vertex, predecessor):
        """Añade un predecesor al conjunto de predecesores de un vértice (para grafo dirigido)."""
        if vertex not in self.predecessors:
            self.predecessors[vertex] = set()
        self.predecessors[vertex].add(predecessor)

    def add_edge(self, source, target, weight=None):
        """Añade una arista entre dos vértices con un peso. Asegura que no haya bucles ni duplicados."""
        if source == target:
            raise ValueError("No se permiten bucles (vértice origen igual al de destino).")

        # Asegurarse de que los vértices existan en el grafo
        if source not in self.vertices:
            self.add_vertex(source)
        if target not in self.vertices:
            self.add_vertex(target)

        # No agregar arista duplicada
        if target in self.edges.get(source, {}):
            return

        # Añadir la arista
        if source not in self.edges:
            self.edges[source] = {}
        self.edges[source][target] = weight
        self._weight[(source, target)] = weight

        # Actualizar los vecinos y predecesores
        self.__add_neighbors(source, target)
        if self.directed:
            self.__add_predecessors(target, source)
        else:
            self.__add_neighbors(target, source)

    def edge_weight(self, source, target):
        """Devuelve el peso de la arista entre los vértices source y target."""
        return self._weight.get((source, target), None)

    def add_vertex(self, vertex):
        """Añade un nuevo vértice al grafo si no existe."""
        if vertex in self.vertices:
            return False
        self.vertices.add(vertex)
        return True

    def edge_source(self, source, target):
        """Devuelve el vértice de origen de una arista."""
        return source

    def edge_target(self, source, target):
        """Devuelve el vértice de destino de una arista."""
        return target

    def vertex_set(self):
        """Devuelve el conjunto de todos los vértices del grafo."""
        return self.vertices

    def contains_edge(self, source, target):
        """Verifica si existe una arista entre los vértices source y target."""
        return target in self.edges.get(source, {})

    def predecessors(self, vertex):
        """Devuelve los predecesores de un vértice (vecinos en grafo no dirigido)."""
        if self.directed:
            return self.predecessors.get(vertex, set())
        return self.successors.get(vertex, set())

    def successors(self, vertex, traversal_type="FORWARD"):
        """Devuelve los sucesores de un vértice dependiendo del tipo de recorrido."""
        if traversal_type == "FORWARD":
            return self.successors.get(vertex, set())
        elif traversal_type == "BACK":
            return self.predecessors.get(vertex, set())
        else:
            raise ValueError("Tipo de recorrido no válido. Use 'FORWARD' o 'BACK'.")

    def inverse_graph(self):
        """Devuelve el grafo inverso si es dirigido. Si no es dirigido, retorna el grafo original."""
        if not self.directed:
            return self
        
        inverted_graph = Graph(directed=True)
        for source in self.edges:
            for target in self.edges[source]:
                inverted_graph.add_edge(target, source, self.edges[source][target])
        
        return inverted_graph