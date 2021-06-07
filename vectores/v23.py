'''
    Dos vectores de 100 elementos contienen los pesos y las alturas de un grupo de
    alumnos. Un tercer vector contiene el sexo de los alumnos (0 si es hombre, 1 si es
    mujer). Los datos correspondientes a un alumno se encuentran en la mima posición en
    los tres vectores. Escribir un programa que:
        Lea los datos de los 100 alumnos.
        Encuentre el alumno más alto y la alumna más alta.
        Muestre todos los alumnos que midan más de 180cm y pesen menos de 80k.
        Decir si se puede hacer un equipo de baloncesto masculino con estos alumnos (5
        jugadores de más de 190cm).
        Decir si se puede hacer un equipo de equitación femenino (10 alumnas de menos de 50k
        y menos de 160cm).
        Liste todos los alumnos. Indicar: código de alumno, peso, altura y sexo (‘H’ si es hombre
        y ‘M’ si es mujer).
        Liste todas las alumnas de mayor a menor altura.
        Liste todos los alumnos de menor a mayor peso.
        Solicitar los datos de un alumno (sexo, peso y altura) y mostrar:
            El primer alumno que cumpla las condiciones.
            El último alumno que cumpla las condiciones.
'''
import random

pesos = []
altura = []
sexo = []

for i in range(0, 100):
    rand = random.randint(40, 120)
    pesos.append(rand)

for i in range(0, 100):
    rand = random.randint(150, 210)
    altura.append(rand)

for i in range(0, 100):
    rand = random.randint(0, 1)
    sexo.append(rand)


while True:
    print('''
        ---- Bienvenido ----
        [1] Encuentre el alumno mas alto y la alumna mas alta
        [2] Mostrar los alumnos mayores a 180cm y menos de 80kg
        [3] Saber si se puede hacer un equipo de basquet masculino
        [4] Saber si se puede hacer un equipo de equitacion femenino
        [5] Listar todos los alumnos
        [6] Listar todas las alumas de mayor a menor altura
        [7] Listar todos los alumnos de menor a mayor peso
        [8] Solicitar los datos de un alumno
    ''')
    option = int(input('Ingrese el codigo de la accion que quiere realizar: '))

    if option == 1:
        mas_alto = 0
        mas_alta = 0
        i = 0
        for alum in altura:
            alum_id = altura[i]
            if sexo[i] == 0:
                if alum > mas_alto:
                    mas_alto = alum
            else:
                if alum > mas_alta:
                    mas_alta = alum
            i+=1

        print(f'Los alumnos mas altos son: {mas_alto}cm (hombre) y {mas_alta}cm (mujer)')
    elif option == 2:
        mas180_menos80 = 0
        x = 0
        for alum in altura:
            alum_id = altura[x]
            if alum >= 180:
                if pesos[x] <= 80:
                    mas180_menos80 += 1
            x += 1

        print(f'Hay {mas180_menos80} que miden mas de 180cm y pesan menos de 80kg')
    elif option == 3:
        basquet_masc = 0
        y = 0
        for alum in altura:
            alum_id = altura[y]
            if sexo[y] == 0:
                if alum >= 190:
                    basquet_masc += 1

        if basquet_masc >= 5:
            print(f'Se puede hacer un equipo de basquet masculino: {basquet_masc} jugadores mayor a 190cm')
        else:
            print('No se llega a hacer un equipo de basquet masculino')
    elif option == 4:
        equitacion_fem = 0
        z = 0
        for alum in altura:
            alum_id = altura[z]
            if sexo[z] == 1:
                if pesos[z] <= 50 and alum <= 160:
                    equitacion_fem += 1

        if equitacion_fem >= 10:
            print(f'Se puede hacer un equipo de equitacion femenino: {equitacion_fem} jugadoras menor a 160cm y menor a 50kg')
        else:
            print('No se llega a hacer un equipo de equitacion femenino')
    elif option == 5:
        print('Listado de todos los alumnos:')
        print(' ')
        w = 0
        for alum in altura:
            cod = w
            peso = pesos[w]
            tall = altura[w]
            sex = sexo[w]
            if sex == 0:
                sex = 'H'
            else:
                sex = 'M'
            print('Los datos de los alumnos son:')
            print(f'Codigo: {cod}, Peso: {peso}, Altura: {tall}, Sexo: {sex}')
            w += 1
    elif option == 6:
        


