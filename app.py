from repository.repo_json import RepoJson
from services.categoria_service import CategoriaService
from services.producto_service import ProductoService
from services.proveedor_service import ProveedorService
from services.movimiento_service import MovimientoService
from services.kardex_service import KardexService

repo = RepoJson("data/db.json")
srv_categoria = CategoriaService(repo)
srv_producto = ProductoService(repo)
srv_proveedor = ProveedorService(repo)
srv_movimiento = MovimientoService(repo)
srv_kardex = KardexService(repo)


# Inicializa categoría por defecto al arrancar
srv_categoria.verificar_y_crear_categoria_inicial()

def menu_productos():
    opcion = ""
    while opcion != "0":
        print("\n========== GESTIÓN DE PRODUCTOS ==========")
        print("1. Registrar Producto")
        print("2. Listar Productos")
        print("3. Modificar Producto")
        print("4. Eliminar Producto")
        print("0. Volver al menú principal")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            srv_producto.registrar_producto()
        elif opcion == "2":
            srv_producto.listar_productos()
        elif opcion == "3":
            srv_producto.modificar_producto()
        elif opcion == "4":
            srv_producto.eliminar_producto()

def menu_proveedores():
    opcion = ""
    while opcion != "0":
        print("\n========== GESTIÓN DE PROVEEDORES ==========")
        print("1. Registrar Proveedor")
        print("2. Listar Proveedores")
        print("3. Modificar Proveedor")
        print("4. Eliminar Proveedor")
        print("0. Volver al menú principal")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            srv_proveedor.registrar_proveedor()
        elif opcion == "2":
            srv_proveedor.listar_proveedores()
        elif opcion == "3":
            srv_proveedor.modificar_proveedor()
        elif opcion == "4":
            srv_proveedor.eliminar_proveedor()

def menu_operaciones_adicionales():
    opcion = ""
    while opcion != "0":
        print("\n========== OPERACIONES Y MÉTRICAS ==========")
        print("1. Alerta de Stock Mínimo")
        print("2. Margen de Ganancia por Producto")
        print("3. Índice de Rotación de Inventario")
        print("4. Top Productos de Ingresos (Ranking)")
        print("0. Volver al menú principal")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            srv_kardex.reporte_alerta_stock_minimo()
        elif opcion == "2":
            srv_kardex.reporte_margen_ganancia()
        elif opcion == "3":
            srv_kardex.calcular_rotacion_inventario()
        elif opcion == "4":
            srv_kardex.top_productos_ingresos()

def menu_principal():
    opcion = ""
    while opcion != "0":
        print("\n===== SISTEMA DE GESTIÓN FERRETERÍA ======")
        print("1. Gestión de Almacén (Productos)")
        print("2. Gestión de Proveedores")
        print("3. Registrar Movimiento (Compra / Venta en Kardex)")
        print("4. Módulo de Analíticas y Alertas Extra")
        print("0. Salir")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            menu_productos()
        elif opcion == "2":
            menu_proveedores()
        elif opcion == "3":
            srv_movimiento.registrar_movimiento_kardex()
        elif opcion == "4":
            menu_operaciones_adicionales()
        elif opcion == "0":
            print("Saliendo del sistema de ferretería...")
        else:
            print("Opción incorrecta.")

if __name__ == "__main__":
    menu_principal()