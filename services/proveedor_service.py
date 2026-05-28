from models.proveedor import Proveedor
from utils.generador_id import generar_id_secuencial
from utils.validaciones import pedir_texto, pedir_entero, validar_identificacion_ecuatoriana

class ProveedorService:
    def __init__(self, repo):
        self.repo = repo

    '''CRUD PROVEEDOR'''
    def registrar_proveedor(self):
        print("\n====== REGISTRAR PROVEEDORES ======")
        identificacion = pedir_texto("RUC / Cédula del Proveedor: ")

        es_valido, ruc = validar_identificacion_ecuatoriana(identificacion)
        
        if not es_valido:
            print(" ERROR: El número ingresado no es una cédula o RUC ecuatoriano válido.")
            return
        
        if self.repo.buscar_por_campo("proveedores", "ruc", ruc):
            print("Error: Ya existe un proveedor registrado bajo ese RUC.")
            return
        nombre = pedir_texto("Razón Social / Nombre Completo: ")
        telefono = pedir_texto("Teléfono de Contacto: ")
        direccion = pedir_texto("Dirección de la Empresa: ")

        
        ids_input = input("IDs de productos asociados: ")
        productos_asociados = []
        if ids_input.strip():
            productos_asociados = [int(x.strip()) for x in ids_input.split(",") if x.strip().isdigit()]
        
        lista_prov = self.repo.listar("proveedores", solo_activos=False)
        nuevo_prov = Proveedor(
            generar_id_secuencial(lista_prov), ruc, nombre, telefono, direccion, productos_asociados, True
        )
        self.repo.guardar("proveedores", nuevo_prov.convertir_a_diccionario())
        print("Proveedor añadido satisfactoriamente al sistema.")

    def listar_proveedores(self):
        print("\n====== LISTADO DE PROVEEDORES REGISTRADOS ======")
        proveedores = self.repo.listar("proveedores")
        if not proveedores:
            print("No existen proveedores activo en el sistema.")
            return
        for prov in proveedores:
            print(f"ID: {prov['id']} | RUC: {prov['ruc']} | Nombre: {prov['nombre']} | Prod. Asociados (IDs): {prov['productos_asociados']}")

    def modificar_proveedores(self):
        print("\n====== MODIFICAR PROVEEDORES ======")
        id_prov = pedir_entero("Ingrese el ID del proveedor: ")
        prov = self.repo.buscar_por_id("proveedores", id_prov)
        if not prov:
            print("Proveedor no localizado.")
            return
        
        n_nombre = input(f"Nombre / Razón Social ({prov['nombre']}): ")
        n_tel = input(f"Teléfono ({prov['telefono']}): ")

        nuevos_datos = {
            "nombre": n_nombre if n_nombre.strip() else prov["nombre"],
            "telefono": n_tel if n_tel.strip() else prov["telefono"]
        }
        self.repo.actualizar("proveedores", id_prov, nuevos_datos)
        print("Información de proveedor actualizada.")

    
    def eliminar_proveedor(self):
        print("\n====== ELIMINAR PROVEEDORES ======")
        id_prov = pedir_entero("Ingrese el ID del proveedor a eliminar: ")
        if self.repo.eliminar("proveedores", id_prov):
            print("El proveedor ha sido dado de baja.")
        else:
            print("No se encontró el proveedor solicitado.")