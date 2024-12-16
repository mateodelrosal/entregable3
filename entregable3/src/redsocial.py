from typing import Dict, List
from datetime import date

class E_grafo:
    """Clase base para representar un grafo. Aquí implementaremos lo básico para Red_social."""
    def __init__(self, tipo_grafo: str = 'no dirigido', tipo_recorrido: str = 'BACK'):
        self.tipo_grafo = tipo_grafo
        self.tipo_recorrido = tipo_recorrido
        self.vertices = {}  # Diccionario para almacenar los vértices (usuarios)
        self.aristas = []   # Lista para almacenar las relaciones (aristas)
    
    def add_vertex(self, vertex):
        """Agrega un vértice (usuario) al grafo."""
        if vertex.dni not in self.vertices:
            self.vertices[vertex.dni] = vertex
            return True
        return False
    
    def add_edge(self, source, target, interacciones, dias_activa):
        """Agrega una arista (relación) entre dos usuarios."""
        if source.dni in self.vertices and target.dni in self.vertices and source.dni != target.dni:
            self.aristas.append({'source': source, 'target': target, 'interacciones': interacciones, 'dias_activa': dias_activa})
            return True
        return False

class Usuario:
    """Clase que representa un usuario en el sistema."""
    def __init__(self, dni: str, nombre: str, apellidos: str, fecha_nacimiento: date):
        self.dni = dni
        self.nombre = nombre
        self.apellidos = apellidos
        self.fecha_nacimiento = fecha_nacimiento
    
    @classmethod
    def parse(cls, info: str):
        """Método de factoría que convierte una cadena en un objeto Usuario."""
        dni, nombre, apellidos, fecha_nacimiento_str = info.split(',')
        fecha_nacimiento = date.fromisoformat(fecha_nacimiento_str)
        return cls(dni, nombre, apellidos, fecha_nacimiento)
    
    def __str__(self):
        """Representación en cadena del usuario."""
        return f"{self.dni} - {self.nombre}"

class Relacion:
    """Clase que representa una relación entre dos usuarios."""
    _xx_num = 0
    
    def __init__(self, interacciones: int, dias_activa: int):
        Relacion._xx_num += 1
        self.id = Relacion._xx_num
        self.interacciones = interacciones
        self.dias_activa = dias_activa
    
    def __str__(self):
        """Representación en cadena de la relación."""
        return f"({self.id} - días activa: {self.dias_activa} - num interacciones: {self.interacciones})"

class Red_social(E_grafo):
    """Clase que representa una red social modelada como un grafo."""
    
    def __init__(self, tipo_grafo: str = 'no dirigido', tipo_recorrido: str = 'BACK'):
        super().__init__(tipo_grafo, tipo_recorrido)
        self.usuarios_dni: Dict[str, Usuario] = {}  # Diccionario para almacenar los usuarios indexados por su DNI
    
    @classmethod
    def of(cls, tipo_grafo: str = 'no dirigido', tipo_recorrido: str = 'BACK') -> 'Red_social':
        """Método de factoría que crea una nueva instancia de Red_social."""
        return cls(tipo_grafo, tipo_recorrido)
    
    @classmethod
    def parse(cls, usuarios_file: str, relaciones_file: str) -> 'Red_social':
        """Método de factoría que lee los archivos y crea una instancia de Red_social."""
        red_social = cls()
        
        # Leer usuarios desde el archivo
        with open(usuarios, 'r') as f:
            for line in f:
                usuario = Usuario.parse(line.strip())
                red_social.add_vertex(usuario)
        
        # Leer relaciones desde el archivo
        with open(relaciones_file, 'r') as f:
            for line in f:
                dni_origen, dni_destino, interacciones, dias_activa = line.strip().split(',')
                interacciones = int(interacciones)
                dias_activa = int(dias_activa)
                
                usuario_origen = red_social.usuarios_dni.get(dni_origen)
                usuario_destino = red_social.usuarios_dni.get(dni_destino)
                
                if usuario_origen and usuario_destino:
                    red_social.add_edge(usuario_origen, usuario_destino, interacciones, dias_activa)
        
        return red_social
    
    def __str__(self):
        """Representación en cadena de la red social, mostrando los usuarios y sus relaciones."""
        resultado = "Usuarios en la red social:\n"
        for usuario in self.vertices.values():
            resultado += f"{usuario}\n"
        resultado += "\nRelaciones:\n"
        for arista in self.aristas:
            resultado += f"{arista}\n"
        return resultado
