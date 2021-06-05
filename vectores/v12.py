'''
    Leer una lista de n valores reales y calcular la media y obtener la desviación de cada
    uno de los valores respecto a la media (desviación = x[i] - media). El número máximo de
    valores a introducir en 100.
'''

vector = []

print('Llenado del vector')
for i in range(0, 5):
    num = int(input('Ingrese un numero: '))
    vector.append(num)

media = (sum(vector) / len(vector))
print(f'La media del vector es: {media}')

i = 0
while len(vector):
    if i == len(vector):
        break
    desviacion = vector[i] - media
    print(f'La desviacion de {vector[i]} es: {desviacion}')
    i += 1