'''
    Escribir un programa que simule la votación en un festival de Eurovisión. En el
    concurso participan 12 países. Cada país tiene un código asignado, comenzando por el
    0. Cada país vota a 10 países, otorgándoles 1, 2, 3, 4, 5, 6, 7, 8, 10 ó 12 puntos. Para
    cada país se preguntará el código del país que ha obtenido cada una de las puntuaciones.
    Declarar y utilizar un vector para almacenar los puntos que cada país debe otorgar. Este
    vector debe contener los datos: 1, 2, 3, 4, 5, 6, 7, 8, 10, 12 .El programa debe pedir las
    votaciones de todos los países y obtener:
        País ganador del festival.
        País con menos puntos.
        Puntuación media.
        Diferencia de la puntuación de cada país con la media.
'''
import random

votos_paises = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
paises_votaron = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

print('---- Festival de Eurovision ----')
print(' ')
print('La lista de paices son:')
vector_paises = ['Albania', 'Serbia', 'Bulgaria', 'Portugal', 'Islandia', 'Suiza', 'Grecia', 'España', 'Francia', 'Alemania', 'Italia', 'Belgica']
print(' ')
print('Los codigos de los paices son: ')
for pais in vector_paises:
    print(f'{pais}: {vector_paises.index(pais)}')

print(' ')
print('---- Sistema de votacion ----')

continua = True
while continua == True:
    pais_votante = int(input('Ingrese el codigo del pais que va a votar: '))
    if pais_votante < 0 or pais_votante > 11:
        print('Pais invalido')
        break
    
    if paises_votaron[pais_votante] == 1:
        print('No puede votar 2 o mas veces un pais')
        break
    
    while True:
        vector_votos_disponibles = [1, 2, 3, 4, 5, 6, 7, 8, 10, 12]
        print(f'Los votos disponibles son: {vector_votos_disponibles}')
        for voto in vector_votos_disponibles:
            print(f'Voto con valor: {voto}')
            a_quien_vota = random.randint(0, 11)
            print(f'VOTO GENERADO AUTOMATICAMENTE: {a_quien_vota}')
            # a_quien_vota = int(input('Ingrese el codigo del pais al que va a votar: '))
            votos_paises[a_quien_vota] += voto
        paises_votaron[pais_votante] += 1
        break

    for i in paises_votaron:
        if i == 1:
            continua = False
        else:
            continua = True

mas_votos = 0
menos_votos = 0
i = 0
for pais in votos_paises:
    if i == 0:
        menos_votos = pais
    if pais > mas_votos:
        mas_votos = pais
    if pais < menos_votos:
        menos_votos = pais

pais_ganador_index = votos_paises.index(mas_votos)
pais_ganador = vector_paises[pais_ganador_index]
print(f'El pais ganador fue: {pais_ganador} con {mas_votos} votos.')

pais_menor_index = votos_paises.index(menos_votos)
pais_menor = vector_paises[pais_menor_index]
print(f'El pais con menos votos fue: {pais_menor} con {menos_votos} votos.')

media = (sum(votos_paises) / len(votos_paises))
print(f'La puntuacion media fue de {media} votos')


for pais in votos_paises:
    diferencia = pais - media 
    pais_nombre_index = votos_paises.index(pais)
    pais_nombre = vector_paises[pais_menor_index]
    print(f'La diferencia de {pais_nombre} con respecto a la media es: {diferencia}')