class Relacion:
    """Clase que representa una relación entre dos usuarios."""
    
    # Contador de ID único
    _xx_num = 0
    
    def __init__(self, interacciones: int, dias_activa: int):
        """Inicializa una nueva instancia de Relacion con los atributos proporcionados."""
        Relacion._xx_num += 1  # Incrementamos el contador de ID único
        self.id = Relacion._xx_num
        self.interacciones = interacciones
        self.dias_activa = dias_activa

    @classmethod
    def of(cls, interacciones: int, dias_activa: int) -> 'Relacion':
        """Método de factoría que crea e inicializa una nueva instancia de Relacion."""
        return cls(interacciones, dias_activa)
    
    def __str__(self) -> str:
        """Devuelve la representación de la relación como cadena."""
        return f"({self.id} - días activa: {self.dias_activa} - num interacciones: {self.interacciones})"