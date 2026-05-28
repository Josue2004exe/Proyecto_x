from models.producto import Producto
from utils.generador_id import generar_id_secuencial
from utils.validaciones import pedir_decimal, pedir_entero, pedir_texto

class ProductoService:
    def __init__(self, repo):
        self.repo = repo
    

    '''CRUD PRODUCTOS'''
    def registrar_producto(self):
        print("\n====== REGISTRAR PRODUCTO ======")
        codigo = pedir_texto("Código único del producto: ")

        if self.repo.buscar_por_campo("productos", "codigo",codigo):
            print("Error: Ya existe un producto registrado con ese codigo.")
            return

        nombre = pedir_texto("Nombre del artículo: ")
        cat_id = pedir_entero("ID de la categoria asociada: ")

        if not self.repo.buscar_por_id("categorias", int(cat_id)):
            print("Advertencia: Esa categoria no existe actualmente en el sistema.")
            return

        costo = pedir_decimal("Costo unitario inicial (Costo Promedio): $")
        precio = pedir_decimal("Precio de venta al público (PVP): $")
        stock = pedir_entero("Existencias iniciales (Stock): ")
        stock_min =  pedir_entero("Stock mínimo requerido para alerta: ")

        lista_prod = self.repo.listar("productos", solo_activos=False)
        nuevo_prod = Producto(
            generar_id_secuencial(lista_prod),
            codigo, nombre, cat_id, precio, costo, stock, stock_min, True
        )
        self.repo.guardar("productos", nuevo_prod.convertir_a_diccionario())
        print(f"Producto {nombre} registrado de manera correcta.")
    
    
    def listar_productos(self):
        print("\n====== LISTADO DE PRODUCTOS EN EXISTENCIA ======")
        productos = self.repo.listar("productos")
        if not productos:
            print("No se registran artículos activos en el inventario.")
            return
        for p in productos:
            print(f"ID: {p['id']} | Código: {p['codigo']} | {p['nombre']} | Stock: {p['stock']} | Mín: {p['stock_minimo']} | PVP: ${p['precio_venta']}")

    def modificar_producto(self):
        print("\n====== LISTADO DE PRODUCTOS EN EXISTENCIA ======")
        id_p = pedir_entero("Ingrese el ID del producto a modificar: ")
        p = self.repo.buscar_por_id("productos", id_p)
        if not p:
            print("No se encontró el producto especificado.")
            return
        
        print("Deje el campo vacío y presione [Enter] para conservar el valor actual.")
        n_nombre = input(f"Nombre actual ({p['nombre']}): ")
        n_precio = input(f"Precio venta actual (${p['precio_venta']}): ")
        n_minimo = input(f"Stock mínimo (${p['stock_minimo']}): ")

        nuevos_datos = {
            "nombre": n_nombre if n_nombre.strip() else p["nombre"],
            "precio_venta": float(n_precio) if n_precio.strip() else p["precio_venta"],
            "stock_minimo": float(n_minimo) if n_minimo.strip() else p["stock_minimo"]
        }
        self.rep.actualizar("productos", id_p, nuevos_datos)
        print("El producto a sido modificado correctamente.")
    
    def eliminar_producto(self):
        print("\n====== PRODUCTO A ELIMINAR DEL INVENTARIO ======")
        id_p = pedir_entero("Ingrese el ID del producto a eliminar: ")
        if self.repo.eliminar_producto_logico("productos", id_p):
            print("Producto eliminado correctamente (Estado cambiando a False).")
        else:
            print("EL ID especificado no pertenece a un producto activo(True).")