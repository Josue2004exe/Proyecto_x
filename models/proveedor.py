class Proveedor:
    def __init__(self, id, ruc, nombre, telefono, direccion, producto_asociado=None, estado=True):
        self.id = id
        self.ruc = ruc
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        self.producto_asociado = producto_asociado if producto_asociado is not None else[]
        self.estado = estado

    def convertir_a_diccionario(self):
        return {
            "id": self.id,
            "ruc": self.ruc,
            "nombre": self.nombre,
            "telefono": self.telefono,
            "direccion": self.direccion,
            "producto_asociado": self.producto_asociado,
            "estado": self.estado
        }