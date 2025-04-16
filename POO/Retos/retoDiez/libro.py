
class Libro:
    contador_libros = 0

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        Libro.contador_libros += 1

    def mostrar_info(self):
        info = {
            "TITULO" : f"{self.titulo}",
            "AUTOR" : f"{self.autor}",
            "PAGINAS" : f"{self.paginas}"
        }
        return info
    
    @staticmethod
    def es_grande(paginas):
        if paginas > 300:
            return True
        return False
    
    @classmethod
    def total_libros(cls):
        return cls.contador_libros
    
        