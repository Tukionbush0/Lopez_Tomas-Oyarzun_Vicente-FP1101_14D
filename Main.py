import Funciones as Biblioteca

#Listas para la biblioteca
lista_libros=[["numero","Nombre","Autor","Año de publicacion","Genero"]]
#probando que funcione
Biblioteca.agregar_libro
Biblioteca.ver_libros
Biblioteca.modificar_libro
Biblioteca.eliminar_libro
#Menu de opciones
while True:
 print("1.- Agregar Libro")
 print("2.- Ver todos los libros")
 print("3.- Modificar un libro")
 print("4.- Eliminar un Libro")
 print("5.- Guardar coleccion en un archivo")
 print("6.- Salir del programa")
 print("")
 input("ingrese una opción: ")
 break