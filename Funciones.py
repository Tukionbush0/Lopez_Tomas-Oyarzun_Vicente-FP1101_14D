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
