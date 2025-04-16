from libro import Libro

libros = []

libro_historia = Libro("Mitologia Nordica", "Enrique Bernandez", 368)
libro_amor = Libro("Me before you", "Jojo Moyes", 480)
libro_fantasia = Libro("Harry Potter and the Philosopher's Stone", "J. K. Rowling", 223)

libros.append(libro_historia)
libros.append(libro_amor)
libros.append(libro_fantasia)

print(libro_historia.mostrar_info())
print(libro_amor.mostrar_info())
print(libro_fantasia.mostrar_info())

print(" ")

for libro in libros:
    if Libro.es_grande(libro.paginas):
        print(f"El libro '{libro.titulo}' es grande")
    else:
        print(f"El libro '{libro.titulo}' es pequenio")

print(" ")

print(f"Numero de libros creados: {Libro.total_libros()}")