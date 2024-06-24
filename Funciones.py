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
    nombre=input("Ingrese nombre del libro=")
    autor=input("Ingrese autor del libro=")
    año=input("Ingrese año de publicacion=")
    genero=input("Ingrese el genero del libro=")

def eliminar_libro(lista_libros):
    numeroeliminar=int(input("Ingrese numero de libro que quiere modificar"))
    if numeroeliminar in lista_libros:
        lista_libros.remove[[numeroeliminar]]
