'''
    Escribir un programa que defina gestione los precios de los N artículos de una tienda.
    El programa debe:
        Leer los precios de compra de los artículos, y almacenarlos en el vector de precios de compra.
        Calcular los precios de venta al público de cada producto, sabiendo que el PVP de un
    artículo es igual al precio de compra, más un 50% (beneficio), más un 16% de IVA. Utilizar
    para ello un nuevo vector de precios de venta.
        Listado por pantalla de ambos precios de todos los artículos de la tienda:
'''

vector_compra = []
vector_venta = []

while True:

    print('''
            ---- Bienvenido ----
            [1] Agregar precio de compra y calcular el precio de venta
            [2] Listado de precios
            [3] Salir
        ''')
    option = int(input('Ingrese la opcion: '))

    if option == 1:
        while True:
            print('--- Agregar un precio de compra ----')
            precio_compra = float(input('Ingrese el precio de compra: $'))
            vector_compra.append(precio_compra)

            item = precio_compra
            venta = ((item * 66) / 100)
            venta_total = venta + item
            vector_venta.append(venta_total)

            continua = input('Vas a agregar otro precio? s/n  ')
            continua = continua.lower()

            if continua == 's':
                continue
            elif continua == 'n':
                break
            else:
                print('Opcion invalida')
                break
    elif option == 2:
        print('Los precios son:')
        print(f'Compra: {vector_compra}')
        print(f'Venta: {vector_venta}')
    elif option == 3:
        print('Chau!')
        break
    else:
        print('Opcion invalida')