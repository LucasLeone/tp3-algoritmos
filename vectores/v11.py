'''
    Escribir un programa que lea dos polinomios de grado 10, como
    máximo y calcule el polinomio producto de ambos simplificado
'''


print('---- 2 Polinomios de grado 10 como maximo ----')
print(' ')
print('---- Primer polinomio ----')

grado1 = int(input('De que grado es el primer polinomio? '))
pol1 = []

for i in range(1, grado1 + 1):
    num = int(input(f'Ingrese el valor de X{i}: '))
    pol1.append(num)

const1 = int(input('Ingrese el valor de la constante: '))
pol1.append(const1)

print('---- Segundo polinomio ----')

grado2 = int(input('De que grado es el segundo polinomio? '))
pol2 = []

for i in range(1, grado1 + 1):
    num = int(input(f'Ingrese el valor de X{i}: '))
    pol2.append(num)

const2 = int(input('Ingrese el valor de la constante: '))
pol2.append(const2)


# NO TERMINADOOOO