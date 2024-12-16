import unittest

class TestGraphAndDFS(unittest.TestCase):

    def test_add_vertex(self):
        """Verifica que los vértices se agregan correctamente al grafo."""
        graph = Graph()
        graph.add_vertex("A")
        self.assertIn("A", graph.adjacency_list)  # A debe estar en la lista de adyacencia

    def test_add_edge(self):
        """Verifica que las aristas se agregan correctamente entre vértices."""
        graph = Graph()
        graph.add_edge("A", "B")
        self.assertIn("B", graph.get_neighbors("A"))  # B debe ser vecino de A
        self.assertIn("A", graph.get_neighbors("B"))  # A debe ser vecino de B (grafo no dirigido)

    def test_dfs_traversal(self):
        """Verifica que el recorrido en profundidad funciona correctamente."""
        graph = Graph()
        graph.add_edge("A", "B")
        graph.add_edge("A", "C")
        graph.add_edge("B", "D")

        dfs = RecorridoEnProfundidad.of(graph)
        dfs.traverse("A")

        # Verificamos que el árbol de recorrido contenga los vértices en el orden esperado
        self.assertIn("A", dfs._tree)  # A debe estar en el árbol de recorrido
        self.assertIn("B", dfs._tree)  # B debe estar en el árbol de recorrido
        self.assertIn("C", dfs._tree)  # C debe estar en el árbol de recorrido
        self.assertIn("D", dfs._tree)  # D debe estar en el árbol de recorrido

    def test_path_to_origin(self):
        """Verifica que el método path_to_origin funcione correctamente."""
        graph = Graph()
        graph.add_edge("A", "B")
        graph.add_edge("B", "C")
        graph.add_edge("C", "D")

        dfs = RecorridoEnProfundidad.of(graph)
        dfs.traverse("D")  # Comenzamos desde D

        # Verificamos el camino desde D hasta A
        path = dfs.path_to_origin("D")
        self.assertEqual(path, ["A", "B", "C", "D"])  # El camino debe ser [A, B, C, D]

    def test_origin(self):
        """Verifica que el método origin funcione correctamente."""
        graph = Graph()
        graph.add_edge("A", "B")
        graph.add_edge("B", "C")
        graph.add_edge("C", "D")

        dfs = RecorridoEnProfundidad.of(graph)
        dfs.traverse("D")

        # Verificamos que el origen del vértice "D" sea A
        self.assertEqual(dfs.origin("D"), "A")

    def test_groups(self):
        """Verifica que los vértices se agrupen correctamente según su origen en el recorrido DFS."""
        graph = Graph()
        graph.add_edge("A", "B")
        graph.add_edge("A", "C")
        graph.add_edge("C", "D")

        dfs = RecorridoEnProfundidad.of(graph)
        dfs.traverse("A")

        # Verificamos que los grupos se formen correctamente
        groups = dfs.groups()
        self.assertIn("A", groups)  # El origen A debe estar en los grupos
        self.assertIn("B", groups["A"])  # B debe ser un vecino de A
        self.assertIn("C", groups["A"])  # C debe ser un vecino de A
        self.assertIn("D", groups["C"])  # D debe ser un vecino de C

if __name__ == "__main__":
    unittest.main()