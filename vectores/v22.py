'''
    Escribir un programa que declare un vector de 20 números reales, correspondientes a
    las notas de un grupo de alumnos. El vector debe ser leído por teclado, y posteriormente
    debe ser ordenado mediante el método de la burbuja. Una vez ordenado, debe ser escrito
    por pantalla.
'''

vector = []

print('---- Llenado de la lista de notas ----')
for i in range(0, 20):
    num = float(input('Ingrese la nota: '))
    vector.append(num)

print('---- Ordenamiento burbuja ----')
for i in range(1, len(vector)):
    for j in range(0, len(vector) - i):
        if (vector[j+1] <  vector[j]):
            aux = vector[j]
            vector[j] = vector[j+1]
            vector[j+1] = aux

print(f'El vector ordenado es:')
print(vector)