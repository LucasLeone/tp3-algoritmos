'''
    Escribir un programa que lea un vector de números enteros y 
    lo modifique sumándole una centena a cada elemento.
'''

vector = list()

i = 0

while i < 5:
    num = int(input('Ingrese un numero: '))
    vector.append(num)
    i += 1

z = 0
while z < len(vector):
    vector[z] += 100
    z += 1
    print(vector)
