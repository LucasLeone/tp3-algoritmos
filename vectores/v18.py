'''
    Escribir un programa para gestionar las votaciones a delegado de clase de una clase
    de 30 alumnos. La forma de identificar a un alumno es por el número de orden en la lista
    de clase (de 1 a 30). Teniendo en cuenta la legalidad vigente, antes de comenzar unas
    votaciones, ningún candidato puede tener ningún voto, todos los votos valen igual y
    nadie puede votar dos o más veces. El
    programa debe presentar un menú con las
    siguientes opciones:
    Consulta de Votos de un alumno: el usuario introduce el número de orden de un alumno,
    y el programa devuelve el número actual de votos que tiene dicho alumno.
    Votar a un alumno: el usuario introduce el número de orden de un alumno, y el programa
    incrementa en uno el número de votos que tiene dicho alumno.
    Listado: se presenta por pantalla un listado con el número de orden de cada alumno y el
    número de votos recibido.
'''
# LLENADO DE VECTORES
ALUMNOS = 30
vector_alumnos = []

for alum in range(1, ALUMNOS + 1):
    vector_alumnos.append(alum)

print('La lista de alumnos es: ')
print(vector_alumnos)
print(' ')

vector_votos = []
for x in range(1, ALUMNOS + 2):
    vector_votos.append(0)

vector_votantes = []
for x in range(1, ALUMNOS + 2):
    vector_votantes.append(0)


while True:
    print('''
        ---- Bienvenido ----
        [1] Consultar votos de un alumno
        [2] Votar a un alumno
        [3] Listado de votos
        [4] Salir
    ''')
    option = int(input('Ingrese la opcion: '))

    if option == 1:
        consulta = int(input('Que alumno quiere consultar? '))
        consulta_id = vector_votos[consulta] + 1
        votos = vector_votos[consulta_id]
        print(f'El alumno {consulta} tiene {votos} votos.')
    elif option == 2:
        while True:
            print('---- Sistema de votacion ----')
            votante = int(input('Ingrese el numero del alumno que va a votar: '))
            
            if votante < 1 or votante > 30:
                print('Alumno inexistente')
                break

            votante_var = vector_alumnos.index(votante)
            
            votoa = int(input('A quien vota? '))


            if votoa < 1 or votoa > 30:
                print('No existe ese alumno')
                break

            votoa_var = vector_alumnos.index(votoa) + 1

            vector_votos[votoa_var] += 1

            if vector_votantes[votante_var] == 0:
                vector_votantes[votante_var] = 1
                print('Voto agregado')
            else:
                print('No puede volver a votar')

            continua = input('Quiere agregar otro voto? s/n  ')
            continua = continua.lower()
            if continua == 's':
                continue
            elif continua == 'n':
                break
            else:
                print('Opcion invalida')
                break
    elif option == 3:
        vector_votantes.pop(0)
        vector_votos.pop(0)
        print('El listado de votos es:')
        print(f'Lista de votantes: {vector_votantes}')
        print(len(vector_votantes))
        print(f'Lista de alumnos votados: {vector_votos}')
        print(len(vector_votos))
    elif option == 4:
        print('Chau!')
        break
    else:
        print('Opcion invalida')
        continue
    
