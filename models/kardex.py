class Kardex:
    def __init__(self, id, producto_id, movimiento_id, saldo_stock,
                detalle, estado=True):
        self.id = id
        self.producto_id = producto_id
        self.movimiento_id = movimiento_id
        self.saldo_stock = saldo_stock
        self.detalle = detalle
        self.estado = estado

    def convertir_a_diccionario(self):
        return{
            "id" : self.id,
            "producto_id" : self.producto_id,
            "movimiento_id" : self.movimiento_id,
            "saldo_stock" : self.saldo_stock,
            "detalle" : self.detalle,
            "estado" : self.estado
        }
        