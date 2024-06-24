import Funciones as biblioteca


#Listas para la biblioteca
lista_libros=[["numero","Nombre","Autor","Año de publicacion","Genero"]]
while True:
 print("1.- Agregar Libro")
 print("2.- Ver todos los libros")
 print("3.- Modificar un libro")
 print("4.- Eliminar un Libro")
 print("5.- Salir del programa")
 print("")
 ops=input("ingrese una opción: ")
 if ops=="1":
    biblioteca.agregar_libro(lista_libros)
 elif ops=="2":
    biblioteca.ver_libros(lista_libros)
 elif ops=="3":
    biblioteca.modificar_libro(lista_libros)
 elif ops=="4":
    biblioteca.eliminar_libro(lista_libros)
 elif ops=="5":
    print("Saliendo de programa")
    break
 else:
    print("opcion no valida")