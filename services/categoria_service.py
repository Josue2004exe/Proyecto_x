from models.categoria import Categoria

class CategoriaService:
    def __init__(self, repo):
        self.repo = repo
    
    def verificar_y_crear_categoria_inicial(self):
        cats = self.repo.listar("categorias", solo_activos=False)
        if not cats:
            c = Categoria(1, "Ferretería General", "Herramientas y consumibles")
            self.repo.guardar("categorias", c.convertir_a_diccionario())