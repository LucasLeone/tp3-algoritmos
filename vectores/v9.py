'''
    Implementar un programa que lea las notas de todos los alumnos de una clase para
    una asignatura, calcule la media, y determine cuántos alumnos superan o igualan la
    media y cuántos están por debajo de la misma. Calcular la nota máxima y mínima.
'''

alumnos = int(input('Ingrese la cantidad de alumnos: '))
if alumnos <= 0:
    print('No se puede tener menos de 0 alumnos')
    quit()

vector = []

for x in range(0, alumnos):
    nota = float(input('Ingrese la nota del alumno: '))
    vector.append(nota)

media = (sum(vector) / len(vector))
print(f'La media es: {media}')

alumnos_mayores = 0
alumnos_menores = 0

for alum in vector:
    if alum >= media:
        alumnos_mayores += 1
    else:
        alumnos_menores += 1

print(f'Hay un total de {alumnos_mayores} que superan la media y {alumnos_menores} que no la superan')

print(f'La nota maxima fue: {max(vector)}')
print(f'La nota minima fue: {min(vector)}')