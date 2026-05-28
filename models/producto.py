class Producto:
    def __init__(self, id, codigo, nombre, categoria_id, precio_venta, 
                costo_promedio, stock, stock_minimo, estado=True):
        self.id = id
        self.codigo = codigo
        self.nombre = nombre
        self.categoria_id = categoria_id
        self.precio_venta = precio_venta
        self.costo_promedio = costo_promedio
        self.stock = stock
        self.stock_minimo = stock_minimo
        self.estado = estado

    def convertir_a_diccionario(self):
        return {
            "id": self.id,
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria_id": self.categoria_id,
            "precio_venta": self.precio_venta,
            "costo_promedio": self.costo_promedio,
            "stock": self.stock,
            "stock_minimo" : self.stock_minimo,
            "estado" : self.estado
        }