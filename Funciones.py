def agregar_libro(lista_libros):
    numero=1
    nombre=input("Ingrese nombre del libro=")
    autor=input("Ingrese autor del libro=")
    año=input("Ingrese año de publicacion=")
    genero=input("Ingrese el genero del libro=")
    lista_libros[[numero,nombre,autor,año,genero]]
    numero=numero+1

def ver_libros(lista_libros):
    for i in lista_libros:
        print(i)
        
def modificar_libro(lista_libros):
    numeromodificar=int(input("Ingrese el numero del libro que desea modificar"))
    if numeromodificar in lista_libros:
     nombre=input("Ingrese nombre del libro=") 
     lista_libros.append[numeromodificar][1]=nombre
     autor=input("Ingrese autor del libro=")
     lista_libros.append[numeromodificar][2]=autor
     año=input("Ingrese año de publicacion=")
     lista_libros.append[numeromodificar][3]=año
     genero=input("Ingrese el genero del libro=")
     lista_libros.append[numeromodificar][4]=genero

def eliminar_libro(lista_libros):
    numeroeliminar=int(input("Ingrese numero de libro que quiere modificar"))
    if numeroeliminar in lista_libros:
        lista_libros.remove[[numeroeliminar]]
        
def menu_ops(lista_libro,biblioteca):
    while True:
        print("1.- Agregar Libro")
        print("2.- Ver todos los libros")
        print("3.- Modificar un libro")
        print("4.- Eliminar un Libro")
        print("5.- Guardar coleccion en un archivo")
        print("6.- Salir del programa")
        print("")
        ops=input("ingrese una opción: ")
        if ops==1:
            biblioteca.agregar_libro(lista_libro)
        elif ops==2:
            biblioteca.ver_libros(lista_libro)
        elif ops==3:
            biblioteca.modificar_libro(lista_libro)
        elif ops==4:
            biblioteca.eliminar_libro(lista_libro)
        elif ops==5:
            print
        elif ops==6:
            print("Saliendo de programa")
            break
        else:
            print("opcion no valida")
        
            

