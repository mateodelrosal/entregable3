import unittest

class TestGraph(unittest.TestCase):

    def test_add_vertex(self):
        """Test para añadir vértices al grafo."""
        graph = Graph()
        self.assertTrue(graph.add_vertex("A"))  # Añadir un vértice nuevo debe devolver True
        self.assertFalse(graph.add_vertex("A"))  # Añadir un vértice repetido debe devolver False
        self.assertIn("A", graph.vertex_set())  # El vértice A debe estar en el conjunto de vértices

    def test_add_edge(self):
        """Test para añadir aristas entre vértices."""
        graph = Graph()
        graph.add_vertex("A")
        graph.add_vertex("B")

        # Añadir una arista entre A y B
        graph.add_edge("A", "B", 5)
        self.assertTrue(graph.contains_edge("A", "B"))  # Debe existir una arista de A a B
        self.assertEqual(graph.edge_weight("A", "B"), 5)  # El peso de la arista debe ser 5

        # Intentar añadir una arista duplicada (no debe hacer nada)
        graph.add_edge("A", "B", 5)
        self.assertEqual(len(graph.edges["A"]), 1)  # Solo debe haber una arista de A a B

        # Probar con grafo no dirigido
        graph_no_directed = Graph(directed=False)
        graph_no_directed.add_vertex("A")
        graph_no_directed.add_vertex("B")
        graph_no_directed.add_edge("A", "B", 5)
        self.assertTrue(graph_no_directed.contains_edge("B", "A"))  # En grafo no dirigido debe haber arista de B a A también

    def test_predecessors_and_successors(self):
        """Test para obtener predecesores y sucesores de un vértice."""
        graph = Graph(directed=True)
        graph.add_vertex("A")
        graph.add_vertex("B")
        graph.add_edge("A", "B", 3)

        # Verificar sucesores y predecesores
        self.assertEqual(graph.successors("A"), {"B"})  # A tiene como sucesor a B
        self.assertEqual(graph.predecessors("B"), {"A"})  # B tiene como predecesor a A

    def test_inverse_graph(self):
        """Test para obtener el grafo inverso."""
        graph = Graph(directed=True)
        graph.add_vertex("A")
        graph.add_vertex("B")
        graph.add_edge("A", "B", 10)

        # Invertir el grafo
        inverted_graph = graph.inverse_graph()
        self.assertTrue(inverted_graph.contains_edge("B", "A"))  # El grafo invertido debe tener una arista de B a A

        # Verificar que el grafo original no ha cambiado
        self.assertTrue(graph.contains_edge("A", "B"))  # El grafo original sigue teniendo la arista de A a B

    def test_edge_exceptions(self):
        """Test para manejar errores como bucles no permitidos."""
        graph = Graph()
        graph.add_vertex("A")

        # Intentar añadir una arista de un vértice a sí mismo (debe lanzar ValueError)
        with self.assertRaises(ValueError):
            graph.add_edge("A", "A", 5)

if __name__ == "__main__":
    unittest.main()