def agregar_libro(lista_libros):
    nombre=input("Ingrese nombre del libro=")
    autor=input("Ingrese autor del libro=")
    año=input("Ingrese año de publicacion=")
    genero=input("Ingrese el genero del libro=")
    lista_libros[[nombre,autor,año,genero]]
def ver_libros(lista_libros):
    for i in lista_libros:
        print(i)
