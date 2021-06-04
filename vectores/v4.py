'''
    Leer un vector de enteros y sacar por pantalla primero todos los elementos
    introducidos en posiciones pares y después todos los de posiciones impares.
'''

vector = list()

tamaño = int(input('Ingrese el tamaño del vector: '))
if tamaño <= 0:
    print('El tamaño no puede ser menor o igual a 0')
    quit()

for x in range(0, tamaño):
    num = int(input('Ingrese el numero: '))
    vector.append(num)

vector_par = list()
vector_impar = list()

for i in range(0, tamaño):
    if i % 2 == 0:
        vector_par.append(vector[i])
    else:
        vector_impar.append(vector[i])

print(f'Vector con posiciones pares: {vector_par}')
print(f'Vector con posiciones impares: {vector_impar}')