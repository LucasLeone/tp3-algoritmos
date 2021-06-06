'''
    Se define un vector de enteros como alternado si el valor de cada componente es de
    signo contrario a la componente anterior. Escribir un programa que lea desde teclado un
    vector de enteros, compruebe si es alternado, y finalmente imprima por pantalla un
    mensaje indicando si es alternado o no. Un ejemplo de vector alternado:
        [-2, 3, -4, 1, -90, 2]
'''

magnitud = int(input('Ingrese el tamaño del vector: '))

vector = []

for x in range(0, magnitud):
    num = int(input('Ingrese un numero: '))
    if num == 0:
        print('El 0 no puede ser ingresado porque es un valor nulo')
    vector.append(num)

i = 0
esmayor = bool()

alternado = bool()

for num in vector:
    if i == 0:
        if num > 0:
            esmayor = True
        else:
            esmayor = False
        i += 1

    if i > 0 and i < len(vector) -1:
        if esmayor == True:
            if vector[i] < 0:
                alternado = True
            else:
                alternado = False
        elif esmayor == False:
            if vector[i] > 0:
                alternado = True
            else:
                alternado = False
        i += 1


if alternado == True:
    print('EL vector es alternado')
else:
    print('No es alternado')

print(vector)