class Categoria:
    def __init__(self, id, nombre, descripcion, estado=True):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.estado = estado

    def convertir_a_diccionario(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "estado": self.estado,
        }
    
