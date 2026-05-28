from datetime import datetime
from models.movimiento_inventario import MovimientoInventario
from models.kardex import Kardex
from utils.generador_id import generar_id_secuencial
from utils.validaciones import pedir_texto, pedir_decimal, pedir_entero

class MovimientoService:
    def __init__(self, repo):
        self.repo = repo
    
    def registrar_movimiento_kardex(self):
        print("\n====== NUEVO MOVIMIENTO DE INVENTARIO (KARDEX) ======")
        print("1. COMPRA (Incrementa Stock y recalcula Costo Promedio)")
        print("2. VENTA (Disminuye Stock si hay disponibilidad)")
        opc = pedir_texto("Seleccione Tipo (1 o 2): ")

        if opc not in ["1", "2"]:
            print("Opción inválida.")
            return
        
        tipo = "COMPRA" if opc == "1" else "VENTA"
        id_p = pedir_entero("ID del Producto afectado: ")
        p = self.repo.buscar_por_id("productos", id_p)


        if not p:
            print("El producto no existe.")
            return
        
        cantidad = pedir_entero(f"Cantidad a procesar por {tipo}: ")
        if cantidad <= 0:
            print("La cantidad debe ser mayor a cero.")
            return
        
        precio_u = pedir_decimal("Precio unitario de la transacción: ")
        #El metodo .now()sirve para tomar la fecha y hora exacta del momento.
        fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        #Reglas de Negocio de Stock y Costo Promedio ponderado
        nuevo_stock = p["stock"]
        if tipo == "COMPRA":
        #Recalcular Costo Promedio Ponderado
            costo_total_antiguo = p["stock"] * p["costo_promedio"]
            costo_compra_nueva = cantidad * precio_u
            nuevo_stock = p["stock"] + cantidad
            nuevo_costo_prom = (costo_total_antiguo + costo_compra_nueva ) / nuevo_stock
            p["costo_promedio"] = round(nuevo_costo_prom, 4)
            p["stock"] = nuevo_stock
        else:
            if p["stock"] < cantidad:
                print(f"Error: Stock insuficiente. Stock actual disponible: {p['stock']}")
                return
            nuevo_stock  = p["stock"] - cantidad
            p["stock"] = nuevo_stock
        
        #1. Guardar Movimiento
        list_movs = self.repo.listar("movimientos", solo_activos=False)
        id_mov = generar_id_secuencial(list_movs)
        mov = MovimientoInventario(id_mov, tipo, id_p, cantidad, precio_u, fecha_actual)
        self.repo.guardar("movimientos", mov.convertir_a_diccionario())
        
        #2. Actualizar Producto Fisicamente en JSON
        self.repo.actualizar("productos", id_p, {"stock": p["stock"], "costo_promedio": p["costo_promedio"]})

        #3. Registrar Transacción Histórica en Kardex
        lista_kardex = self.repo.listar("kardex", solo_activos=False)
        detalle = f"Registro de {tipo} según transacción comercial externa."
        kd = Kardex(generar_id_secuencial(lista_kardex), id_p, id_mov, nuevo_stock, detalle)
        self.repo.guardar("kardex", kd.convertir_a_diccionario())

        print(f"Transacción procesada con éxito. Stock resultante de la entidad: {nuevo_stock}")
        