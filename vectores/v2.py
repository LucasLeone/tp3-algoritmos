'''
    Escribir un programa que declare un vector de 10 números enteros, pida al usuario
    cada una de sus Componentes y luego:
            . Los escriba por pantalla.
            . Los escriba en orden inverso.
            . Muestre por pantalla la suma y la media
'''

i = 0

vector = list()

while i < 5:
    print('--- Nuevo numero ---')
    num = int(input('Ingrese un numero: '))
    
    vector.append(num)

    i += 1

print(f'El vector es: {vector}')

vector_inverso = vector[::-1]
print(f'El vector inverso es: {vector_inverso}')

suma = sum(vector)
print(f'La suma del vector es: {suma}')

valores = len(vector)
total = sum(vector)
print(f'La media del vector es: {total / valores}')