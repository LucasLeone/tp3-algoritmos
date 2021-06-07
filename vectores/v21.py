'''
    Se desea utilizar un vector para almacenar una lista de códigos numéricos de libros
    en una biblioteca. Se pueden almacenar como máximo N libros, aunque no todas las posiciones tienen
    porqué estar ocupadas. El programa debe presentar un menú que contenga las siguientes opciones:
            Añadir un libro.
            Eliminar un libro
            Listar los libros
            Salir.
                • Añadir un libro: se lee un nuevo código y se añade el nuevo libro al vector. La inserción
                debe hacerse en orden respecto a los libros que ya se han insertado previamente.
                • Eliminar un libro: se pide el código de libro a eliminar. Se busca el libro en el vector. Si
                dicho libro no se encuentra, se debe informar del error por pantalla. Si lo encuentra, debe
                eliminarlo y compactar los valores que restan a la izquierda. Por ejemplo, dado el siguiente vector:
                    [34, 145, 234, 235, 289, 321, blank]
                    Si se eligiera el 235 para eliminar, el vector deberia quedar asi:
                    [34, 145, 234, 235, 289, blank, blank]
                • Listar: se visualizan los códigos de los libros que están presentes en la biblioteca en ese momento.
                • Mientras que el usuario no elija la opción de salir, el algoritmo debe volver a presentar el menú
'''

vector_libros = []

while True:

    print('''
            ---- Bienvenido ----
            [1] Añadir un libro
            [2] Eliminar un libro
            [3] Listar los libros
            [4] Salir
        ''')
    option = int(input('Ingrese la opcion: '))

    if option == 1:
        cod_add = int(input('Ingrese el codigo del libro: '))
        if cod_add in vector_libros:
            print('Ya existe ese libro')
        else:
            print('Libro añadido!')
            vector_libros.append(cod_add)
    elif option == 2:
        cod_del = int(input('Ingrese el codigo del libro que desea eliminar: '))
        if cod_del in vector_libros:
            vector_libros.remove(cod_del)
            print('Libro eliminado!')
        else:
            print('No existe ese libro')
    elif option == 3:
        print('Los codigos de los libros que hay actualmente son:')
        print(vector_libros)
    elif option == 4:
        print('Chau!')
        break
    else:
        print('Opcion invalida')