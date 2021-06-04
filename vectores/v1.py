'''
    Escribir un programa solicite al usuario 100 valores enteros y los almacene en un
    vector. Posteriormente, debe calcular el valor máximo, mínimo y la media
'''

i = 0

vector = list()

# LLENADO DEL VECTOR
while i < 10:
    print('--- Nuevo numero ---')
    num = int(input('Ingrese un numero: '))

    i+=1

    vector.append(num)

# MEDIA
valores = len(vector)
total = sum(vector)
print(f'La media del vector es: {total / valores}')

# MAXIMO
maximo = max(vector)
print(f'El valor maximo es: {maximo}')

# MINIMO
minimo = min(vector)
print(f'El valor minimo es: {minimo}')
