from utils.validaciones import pedir_decimal, pedir_entero, pedir_texto

class KardexService:
    def __init__(self, repo):
        self.repo = repo

        #Adicional 1: AlertaStockMinimo
    def reporte_alerta_stock_minimo(self):
        print("\n====== ALETA DE STOCK MÍNIMO ======")
        productos = self.repo.listar("productos")
        encontrados = False
        for p in productos:
            if p["stock"] <= p["stock_minimo"]:
                print(f"¡ALERTA!  ID: {p['id']} | Producto: {p['nombre']} | Stock Actual: {p['stock']} (Mínimo Permitido: {p['stock_minimo']})")
                encontrados = True
        if not encontrados:
            print("Excelente: Todos los productos se encuentran por encima del stock minimo.")

        #Adicional 2: MargenGananciaPorProducto
    def reporte_margen_ganancia(self):
        print("\n====== MARGEN DE GANANCIA POR PRODUCTO ======")
        print("Fórmula aplicada: (Precio Venta - Costo Promedio) / Precio venta")
        productos = self.repo.listar("productos")
        for p in productos:
            if p["precio_venta"] > 0:
                margen = (p["precio_venta"] - p["costo_promedio"]) / p["precio_venta"]
                #sirve para mostrar un número con exactamente dos decimales después del punto.
                print(f"Producto: {p['nombre']} | PVP: ${p['precio_venta']} | Costo Prom.: ${p['costo_promedio']:.2f} | Margen: {margen * 100:.2f}%")
            else:
                print(f"Producto: {p['nombre']} | Margen no calculable (Precio de venta en 0).")
        
        #Adicional 3: RotacionInventario
    def calcular_rotacion_inventario(self):
        print("\n===== ROTACIÓN DE INVENTARIO EN EL PERIODO =====")
        print("Fórmula: Unidades Vendidas Totales / Stock Promedio del Inventario")
        
        movimientos = self.repo.listar("movimientos")
        productos = self.repo.listar("productos")
        
        if not productos:
            print("No hay productos cargados en base de datos.")
            return

        unidades_vendidas = sum(m["cantidad"] for m in movimientos if m["tipo"] == "VENTA")
        stock_total_actual = sum(p["stock"] for p in productos)
        
        # Simulamos stock promedio usando stock inicial histórico estimado y actual
        stock_promedio = (stock_total_actual + (stock_total_actual + unidades_vendidas)) / 2
        
        if stock_promedio == 0:
            print("No es posible calcular la rotación debido a un inventario sin existencias de stock.")
            return
            
        rotacion = unidades_vendidas / stock_promedio
        print(f"-> Unidades totales despachadas por ventas: {unidades_vendidas}")
        
        print(f"-> Stock promedio calculado en base física: {stock_promedio:.2f} unidades.")
        print(f"-> Índice de Rotación de Inventario: {rotacion:.4f} veces en el ciclo.")

    # Adicional 4: TopProductosPorIngresos
    def top_productos_ingresos(self):
        print("\n===== TOP PRODUCTOS POR INGRESOS (RANKING) =====")
        movimientos = self.repo.listar("movimientos")
        productos = self.repo.listar("productos")

        ingresos_por_producto = {}
        for m in movimientos:
            if m["tipo"] == "VENTA":
                p_id = m["producto_id"]
                subtotal = m["cantidad"] * m["precio_unitario"]
                ingresos_por_producto[p_id] = ingresos_por_producto.get(p_id, 0.0) + subtotal

        ranking = []
        for p_id, total in ingresos_por_producto.items():
            prod_obj = self.repo.buscar_por_id("productos", p_id)
            nombre_p = prod_obj["nombre"] if prod_obj else f"Producto ID {p_id}"
            ranking.append((nombre_p, total))

        # Ordenar de mayor a menor ingreso
        ranking.sort(key=lambda x: x[1], reverse=True)

        if not ranking:
            print("No se registran transacciones de venta que generen ingresos financieros aún.")
            return

        for i, (nombre, total) in enumerate(ranking, start=1):
            print(f"{i}. {nombre} -> Ingresos Totales: ${total:.2f}")