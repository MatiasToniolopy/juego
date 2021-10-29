########################################
#JUEGO TRIVIA DE PREGUNTAS Y RESPUESTAS#
########################################

#CREADOR: MATIAS MANUEL TONIOLO

#VERSION: 1.0

#AÑO 2021

import random
import csv


with open('toniolo1.csv',encoding='utf-8') as mmm:
    data = mmm.readlines()
    

dic = {}

for linea in data:
    pais, capital, continente = linea.split(',')
    dic[pais] = capital
    
    
print('####################################################################')
print('¡¡¡BIENVENIDO A UN NUEVO JUEGO, PONGAMOS A PRUEBA TU CONOCIMIENTO!!!')
print('####################################################################\n')

cantidad_jugadores = int(input('¿De cuantos jugadores sera la partida?: '))
cantidad_turnos = int(input('¿Cuantos turnos jugaran?: '))

puntajes = {}

for i in range(cantidad_jugadores):
    nombre = input('Ingrese el nombre del jugador: ')
    puntajes[nombre] = 0

print()
    

for i in range(cantidad_turnos):
    for nombre in puntajes.keys():
        pais_aleat = random.choice(list(dic.keys()))
        respuesta = input(f'Jugador {nombre}: ¿cual es la capital del pais: {pais_aleat}? ')
        if respuesta == dic[pais_aleat]:
            print('Muy bien, la respuesta es correcta, sumaste un punto')
            puntajes[nombre] += 1
        else:
            print(f'La respuesta es incorrecta, la capital es: {dic[pais_aleat]}\n')

print('#################')
print('FIN DE LA PARTIDA')
print('#################\n')

mmm.close()

def pos (puntajes):
    for i,(nombre,puntajes) in enumerate(sorted(puntajes.items(), key= lambda x: x[1], reverse=True)):
        print(f'El jugador {nombre} obtuvo la {i+1}° posicion con un puntaje de: {puntajes} puntos')
        

pos(puntajes)
