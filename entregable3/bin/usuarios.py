from datetime import date
from typing import Optional

class usuarios:
    """Clase que representa un usuario en el sistema."""
    
    def __init__(self, dni: str, nombre: str, apellidos: str, fecha_nacimiento: date):
        """Inicializa un nuevo usuario con los atributos proporcionados."""
        self.dni = dni
        self.nombre = nombre
        self.apellidos = apellidos
        self.fecha_nacimiento = fecha_nacimiento

    @classmethod
    def of(cls, dni: str, nombre: str, apellidos: str, fecha_nacimiento: date) -> 'usuarios':
        """Método de factoría para crear una nueva instancia de Usuario."""
        return cls(dni, nombre, apellidos, fecha_nacimiento)

    @classmethod
    def parse(cls, info: str) -> 'Usuario':
        """Método de factoría que convierte una cadena de texto en una instancia de usuarios."""
        # Formato esperado: "45718832U,Carlos,Lopez,1984-01-14"
        dni, nombre, apellidos, fecha_nacimiento_str = info.split(',')
        
        # Verificamos que el DNI tenga el formato correcto: 8 dígitos seguidos de una letra
        if len(dni) != 9 or not dni[:-1].isdigit() or not dni[-1].isalpha():
            raise ValueError("DNI no válido")
        
        # Parseamos la fecha de nacimiento
        fecha_nacimiento = date.fromisoformat(fecha_nacimiento_str)
        
        # Comprobamos que la fecha de nacimiento sea anterior a la fecha actual
        if fecha_nacimiento >= date.today():
            raise ValueError("La fecha de nacimiento debe ser anterior a la fecha actual")
        
        return cls(dni, nombre, apellidos, fecha_nacimiento)
    
    def __str__(self) -> str:
        """Devuelve la representación del usuario como cadena: 'dni - nombre'."""
        return f"{self.dni} - {self.nombre}"
    
    # Método adicional para obtener la edad del usuario
    def edad(self) -> int:
        """Calcula y devuelve la edad del usuario en años."""
        today = date.today()
        age = today.year - self.fecha_nacimiento.year
        if today.month < self.fecha_nacimiento.month or (today.month == self.fecha_nacimiento.month and today.day < self.fecha_nacimiento.day):
            age -= 1
        return age