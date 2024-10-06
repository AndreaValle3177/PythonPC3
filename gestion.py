from libro import Libro

class GestionBiblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f"Libro '{libro.titulo}' agregado a la biblioteca.")

    def listar_libros(self):
        if not self.libros:
            print("No hay libros en la biblioteca.")
        else:
            print("Lista de libros en la biblioteca:")
            for libro in self.libros:
                print(libro)

    def buscar_por_titulo(self, titulo):
        resultados = [libro for libro in self.libros if titulo.lower() in libro.titulo.lower()]
        if resultados:
            print("Libros encontrados por título:")
            for libro in resultados:
                print(libro)
        else:
            print("No se encontraron libros con ese título.")

    def buscar_por_autor(self, autor):
        resultados = [libro for libro in self.libros if autor.lower() in libro.autor.lower()]
        if resultados:
            print("Libros encontrados por autor:")
            for libro in resultados:
                print(libro)
        else:
            print("No se encontraron libros de ese autor.")
