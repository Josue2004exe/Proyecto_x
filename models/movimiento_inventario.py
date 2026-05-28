class MovimientoInventario:
    def __init__(self, id, tipo, producto_id, cantidad, precio_unitario,
                fecha, estado=True):
        self.id = id
        self.tipo = tipo
        self.producto_id = producto_id
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
        self.fecha = fecha
        self.estado = estado

    def convertir_a_diccionario(self):
        return{
            "id" : self.id,
            "tipo" : self.tipo,
            "producto_id" : self.producto_id,
            "cantidad" : self.cantidad,
            "precio_unitario" : self.precio_unitario,
            "fecha" : self.fecha,
            "estado" : self.estado
        }
