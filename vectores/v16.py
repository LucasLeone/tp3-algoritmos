'''
    Escribir un programa que calcule los múltiplos de 3, 4, 5, 6 y 7 que hay entre 1 y 100.
    Utilizar un vector para contener los valores 3, 4, 5, 6 y 7.
'''

vector3 = []
vector4 = []
vector5 = []
vector6 = []
vector7 = []

for x in range(2, 101):
    if x % 3 == 0:
        vector3.append(x)
    if x % 4 == 0:
        vector4.append(x)
    if x % 5 == 0:
        vector5.append(x)
    if x % 6 == 0:
        vector6.append(x)
    if x % 7 == 0:
        vector7.append(x)
    
print(f'Los multiplos de 3: {vector3}')
print(f'Los multiplos de 4: {vector4}')
print(f'Los multiplos de 5: {vector5}')
print(f'Los multiplos de 6: {vector6}')
print(f'Los multiplos de 7: {vector7}')
