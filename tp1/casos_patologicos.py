 # -*- coding: utf-8 -*-

from cartas import *

''' Grupo de las rondas:
1 -> Ancho de espada vs cualquier cosa
2 -> Cartas buenas enfrentadas
3 -> Figuras enfrentadas
4 -> Cartas malas enfrentadas
'''

RONDAS_PATOLOGICAS = [
    Ronda(Carta(1, 'E'), Carta(4, 'O'), 1),
    Ronda(Carta(1, 'E'), Carta(7, 'O'), 1),
    Ronda(Carta(1, 'E'), Carta(6, 'E'), 1),
    Ronda(Carta(2, 'B'), Carta(3, 'O'), 2),
    Ronda(Carta(7, 'E'), Carta(7, 'O'), 2),
    Ronda(Carta(1, 'B'), Carta(7, 'O'), 2),
    Ronda(Carta(3, 'E'), Carta(2, 'O'), 2),
    Ronda(Carta('R', 'E'), Carta('S', 'O'), 3),
    Ronda(Carta('S', 'C'), Carta('C', 'O'), 3),
    Ronda(Carta('S', 'C'), Carta('C', 'O'), 3),
    Ronda(Carta(5, 'C'), Carta(7, 'B'), 4),
    Ronda(Carta(4, 'C'), Carta(6, 'O'), 4),
    Ronda(Carta(4, 'C'), Carta(7, 'C'), 4)
]


'''
Grupos: 
        1 manos testigo de si mira la última o no
        
        2 manos "sencillas" que terminen en 2 rondas. 
            Sencillas quiere deir con un claro ganador y todas las rondas carta alta vs baja. 
            Idealmente Carta mejor o igual que un 2 vs más chota que un 2.
            Hacerlas de 3 rondas que después el programa se ocupa de que la tercera se tape si no tiene sentido)

        3 manos "sencillas" que terminen en 3 rondas  Idem.
        
        4 manos con pardas en: 1ra y 2da
            Las rondas no pardadas con un ganador claro.

        5 manos con pardas en 3ra:
            Hipótesis: manos que si vas en orden son manos de 4 rondas.

        6 manos con pardas en 1ra 2da y 3ra:
            Hipótesis: manos que si vas en orden son manos de 4 rondas.

        7 manos "peleadas" todas con figuras.
            todas menores a 2

        8 manos 
            todas menores a 2

        9 manos en donde el que perdió tenía una carta > 3.



Excepto las del grupo 2 todas deberían terminar en 3 rondas.

2 vs 3 nos sirve para ver como afecta la cantidad de manos.

4 vs 5

Ej. de mano en "en python" :

    Mano(Ronda(Carta(3, 'E'), Carta(4, 'C')),       <--- Ronda 1: 3 de copas vs 4 copas.
         Ronda(Carta(7, 'O'), Carta(2, 'O')),       <--- Ronda 2: 
         Ronda(Carta('R', 'O'), Carta(6, 'E')),       <--- Ronda 3 
         2),       <--- Grupo 2

Si es una figura va 'S' 'C' o 'R' como el 'Rey' de la 3er ronda.
Si no, va el número solo como en las dos primeras.

'''

MANOS_PATOLOGICAS = [

'''
El siguiente grupo de manos termina siempre
 en la 2da ronda pero en la tercera el que 
 perdió tiene una carta más alta. 
 Ideales para mostrar sin tapar.
'''

    Mano(Ronda(Carta(2, 'C'), Carta(3, 'C')),
         Ronda(Carta(1, 'O'), Carta(7, 'O')),
         Ronda(Carta(3, 'O'), Carta(5, 'O')),
         1),

    Mano(Ronda(Carta('R', 'E'), Carta(3, 'E')),
         Ronda(Carta(4, 'C'), Carta(7, 'E')),
         Ronda(Carta(2, 'B'), Carta(5, 'B')),
         1),

    Mano(Ronda(Carta(2, 'O'), Carta(7, 'O')),
         Ronda(Carta('C', 'B'), Carta(2, 'B')),
         Ronda(Carta('C', 'O'), Carta(4, 'E')),
         1),

    Mano(Ronda(Carta(2, 'C'), Carta(4, 'E')),
         Ronda(Carta(3, 'C'), Carta('S', 'C')),
         Ronda(Carta(4, 'C'), Carta(1, 'C')),
         1),

    Mano(Ronda(Carta(7, 'O'), Carta(4, 'C')),
         Ronda(Carta(3, 'E'), Carta(2, 'E')),
         Ronda(Carta(6, 'B'), Carta(3, 'O')),
         1),

    Mano(Ronda(Carta(1, 'B'), Carta(3, 'E')),
         Ronda(Carta(3, 'O'), Carta(2, 'O')),
         Ronda(Carta(5, 'C'), Carta(2, 'C')),
         1),

    Mano(Ronda(Carta('R', 'C'), Carta(1, 'O')),
         Ronda(Carta('R', 'E'), Carta(3, 'B')),
         Ronda(Carta(2, 'E'), Carta(7, 'C')),
         1),

    Mano(Ronda(Carta(1, 'E'), Carta(2, 'E')),
         Ronda(Carta(3, 'E'), Carta(3, 'O')),
         Ronda(Carta(5, 'C'), Carta(1, 'B')),
         1),

    Mano(Ronda(Carta('R', 'B'), Carta(2, 'C')),
         Ronda(Carta(2, 'E'), Carta(3, 'E')),
         Ronda(Carta(2, 'O'), Carta(5, 'E')),
         1),

'''
Grupo 2
'''

    Mano(Ronda(Carta(6, 'B'), Carta(3, 'C')),
         Ronda(Carta('R', 'E'), Carta(7, 'O')),
         Ronda(Carta(5, 'B'), Carta(1, 'O')),
         2),   
    Mano(Ronda(Carta(2, 'O'), Carta(5, 'E')),
         Ronda(Carta(3, 'B'), Carta('S', 'C')),
         Ronda(Carta(5, 'B'), Carta('R', 'E')),
         2), 
    Mano(Ronda(Carta(7, 'E'), Carta('R', 'O')),
         Ronda(Carta(3, 'O'), Carta(5, 'B')),
         Ronda(Carta(5, 'E'), Carta('R', 'B')),
         2), 
    Mano(Ronda(Carta('S', 'O'), Carta(1, 'E')),
         Ronda(Carta('R', 'E'), Carta(7, 'E')),
         Ronda(Carta(5, 'B'), Carta('S', 'E')),
         2), 
    Mano(Ronda(Carta(1, 'B'), Carta(5, 'C')),
         Ronda(Carta(2, 'E'), Carta(4, 'O')),
         Ronda(Carta(5, 'E'), Carta(4, 'B')),
         2), 
    Mano(Ronda(Carta(6, 'C'), Carta(1, 'E')),
         Ronda(Carta(4, 'E'), Carta(3, 'B')),
         Ronda(Carta(5, 'E'), Carta(6, 'B')),
         2),
    Mano(Ronda(Carta('C', 'E'), Carta(3, 'O')),
         Ronda(Carta(4, 'O'), Carta(7, 'E')),
         Ronda(Carta(4, 'B'), Carta(6, 'B')),
         2), 
    Mano(Ronda(Carta(7, 'O'), Carta('R', 'C')),
         Ronda(Carta(3, 'B'), Carta(5, 'E')),
         Ronda(Carta(7, 'B'), Carta(6, 'B')),
         2), 
    Mano(Ronda(Carta(1, 'B'), Carta(6, 'B')),
         Ronda(Carta(7, 'E'), Carta('R', 'O')),
         Ronda(Carta(7, 'B'), Carta(6, 'B')),
         2), 
    Mano(Ronda(Carta(3, 'O'), Carta('S', 'E')),
         Ronda(Carta(7, 'O'), Carta(4, 'C')),
         Ronda(Carta(7, 'C'), Carta(6, 'B')),
         2),

'''
Grupo 3
'''

   Mano(Ronda(Carta(2, 'B'), Carta(5, 'C')),
         Ronda(Carta(6, 'B'), Carta(7, 'E')),
         Ronda(Carta('R', 'B'), Carta(3, 'O')),
         3), 
   Mano(Ronda(Carta(3, 'E'), Carta(7, 'B')),
         Ronda(Carta('S', 'B'), Carta(2, 'O')),
         Ronda(Carta(7, 'E'), Carta('R', 'C')),
         3), 
   Mano(Ronda(Carta(1, 'E'), Carta(5, 'O')),
         Ronda(Carta(7, 'C'), Carta(3, 'B')),
         Ronda(Carta(4, 'B'), Carta('R', 'O')),
         3), 
    Mano(Ronda(Carta(6, 'O'), Carta(7, 'E')),
         Ronda(Carta('R', 'B'), Carta(4, 'C')),
         Ronda(Carta(3, 'E'), Carta('S', 'B')),
         3), # No colgar con el grupo.
    Mano(Ronda(Carta(3, 'C'), Carta('R', 'E')),
         Ronda(Carta(6, 'B'), Carta('R', 'O')),
         Ronda(Carta(2, 'E'), Carta(4, 'B')),
         3), # No colgar con el grupo.
    Mano(Ronda(Carta(2, 'C'), Carta(7, 'E')),
         Ronda(Carta('C', 'B'), Carta(6, 'C')),
         Ronda(Carta(2, 'O'), Carta(1, 'B')),
         3), # No colgar con el grupo.
    Mano(Ronda(Carta('S', 'E'), Carta(3, 'B')),
         Ronda(Carta(2, 'O'), Carta(4, 'C')),
         Ronda(Carta(3, 'E'), Carta('R', 'E')),
         3), # No colgar con el grupo.
    Mano(Ronda(Carta(1, 'O'), Carta(1, 'E')),
         Ronda(Carta('R', 'B'), Carta(6, 'O')),
         Ronda(Carta('R', 'C'), Carta(7, 'E')),
         3), # No colgar con el grupo.
    Mano(Ronda(Carta(2, 'E'), Carta(5, 'B')),
         Ronda(Carta('S', 'E'), Carta(3, 'O')),
         Ronda(Carta(7, 'O'), Carta('C', 'C')),
         3), # No colgar con el grupo.
    Mano(Ronda(Carta(6, 'C'), Carta(1, 'B')),
         Ronda(Carta(3, 'E'), Carta('S', 'O')),
         Ronda(Carta(5, 'O'), Carta(1, 'E')),
         3), # No colgar con el grupo.

'''
Grupo 4
 manos con pardas en: 1ra y 2da
            Las rondas no pardadas con un ganador claro.
'''


    Mano(Ronda(Carta(3, 'B'), Carta(3, 'C')),
         Ronda(Carta(2, 'O'), Carta(2, 'E')),
         Ronda(Carta('R', 'E'), Carta(4, 'O')),
         4), # No colgar con el grupo.
    Mano(Ronda(Carta('C', 'O'), Carta('C', 'B')),
         Ronda(Carta(3, 'O'), Carta(3, 'E')),
         Ronda(Carta(2, 'B'), Carta(5, 'C')),
         4), # No colgar con el grupo.
    Mano(Ronda(Carta(6, 'B'), Carta(6, 'C')),
         Ronda(Carta('R', 'E'), Carta('R', 'O')),
         Ronda(Carta(4, 'C'), Carta('R', 'B')),
         4), # No colgar con el grupo.
    Mano(Ronda(Carta(2, 'E'), Carta(2, 'B')),
         Ronda(Carta(3, 'C'), Carta(3, 'E')),
         Ronda(Carta('C', 'B'), Carta(5, 'O')),
         4), # No colgar con el grupo.
    Mano(Ronda(Carta(5, 'C'), Carta(5, 'E')),
         Ronda(Carta('R', 'B'), Carta('R', 'C')),
         Ronda(Carta(4, 'O'), Carta('C', 'E')),
         4), # No colgar con el grupo.
    Mano(Ronda(Carta(3, 'B'), Carta(3, 'O')),
         Ronda(Carta(2, 'E'), Carta(2, 'C')),
         Ronda(Carta(2, 'O'), Carta(5, 'B')),
         4), # No colgar con el grupo.
    Mano(Ronda(Carta('R', 'E'), Carta('R', 'B')),
         Ronda(Carta(3, 'E'), Carta(3, 'O')),
         Ronda(Carta('C', 'O'), Carta(4, 'E')),
         4), # No colgar con el grupo.
    Mano(Ronda(Carta(3, 'C'), Carta(3, 'B')),
         Ronda(Carta('C', 'E'), Carta(11, 'O')),
         Ronda(Carta('5', 'O'), Carta(11, 'B')),
         4), # No colgar con el grupo.
    Mano(Ronda(Carta(5, 'B'), Carta(5, 'E')),
         Ronda(Carta(3, 'O'), Carta(3, 'C')),
         Ronda(Carta(2, 'E'), Carta(6, 'B')),
         4), # No colgar con el grupo.
    Mano(Ronda(Carta(2, 'O'), Carta(2, 'E')),
         Ronda(Carta('C', 'E'), Carta('C', 'C')),
         Ronda(Carta(4, 'E'), Carta('S', 'B')),
         4), # No colgar con el grupo.
    Mano(Ronda(Carta(3, 'B'), Carta(3, 'E')),
         Ronda(Carta('R', 'O'), Carta('R', 'C')),
         Ronda(Carta(6, 'E'), Carta('R', 'B')),
         4), # No colgar con el grupo.











'''
Grupo 7 manos "peleadas" todas con figuras.
        todas menores a 2
'''

    Mano(Ronda(Carta('R', 'B'), Carta('S', 'E')),
         Ronda(Carta('C', 'O'), Carta('R', 'C')),
         Ronda(Carta('S', 'E'), Carta('C', 'B')),
         7), # No colgar con el grupo.
    Mano(Ronda(Carta('R', 'E'), Carta('C', 'B')),
         Ronda(Carta('S', 'E'), Carta('R', 'B')),
         Ronda(Carta('S', 'C'), Carta('C', 'O')),
         7), 
    Mano(Ronda(Carta('S', 'O'), Carta('C', 'B')),
         Ronda(Carta('C', 'C'), Carta('R', 'C')),
         Ronda(Carta('R', 'E'), Carta('S', 'O')),
         7), 

    Mano(Ronda(Carta('R', 'B'), Carta('S', 'C')),
         Ronda(Carta('C', 'O'), Carta('R', 'O')),
         Ronda(Carta('C', 'B'), Carta('S', 'O')),
         7),

    Mano(Ronda(Carta('C', 'E'), Carta('S', 'B')),
         Ronda(Carta('C', 'C'), Carta('R', 'C')),
         Ronda(Carta('C', 'O'), Carta('R', 'E')),
         7),



'''
Grupo 9 manos en donde el que perdió tenía una carta > 3.
'''

    Mano(Ronda(Carta(1, 'B'), Carta('C', 'E')),
         Ronda(Carta('R', 'E'), Carta(2, 'O')),
         Ronda(Carta('4', 'C'), Carta(2, 'E')),
         9,
    Mano(Ronda(Carta('R', 'B'), Carta('C', 'E')),
         Ronda(Carta('R', 'E'), Carta(2, 'O')),
         Ronda(Carta('4', 'C'), Carta(2, 'E')),
         9,

'''
Grupo 5
manos con pardas en 3ra:
Hipótesis: manos que si vas en orden son manos de 4 rondas.
'''
    Mano(Ronda(Carta(1, 'E'), Carta(2, 'B')),
         Ronda(Carta(6, 'C'), Carta('R', 'B')),
         Ronda(Carta(2, 'E'), Carta(2, 'O')),
         5),
    Mano(Ronda(Carta('R', 'O'), Carta(7, 'E')),
         Ronda(Carta(2, 'E'), Carta(6, 'B')),
         Ronda(Carta('R', 'E'), Carta('R', 'C')),
         5),
    Mano(Ronda(Carta(2, 'E'), Carta(1, 'B')),
         Ronda(Carta(3, 'C'), Carta('S', 'E')),
         Ronda(Carta(3, 'O'), Carta(3, 'B')),
         5),
    Mano(Ronda(Carta(2, 'B'), Carta(7, 'O')),
         Ronda(Carta(3, 'C'), Carta('S', 'E')),
         Ronda(Carta(3, 'O'), Carta(3, 'B')),
         5),
    Mano(Ronda(Carta(1, 'B'), Carta('R', 'O')),
         Ronda(Carta(2, 'C'), Carta('7', 'E')),
         Ronda(Carta('S', 'O'), Carta('S', 'B')),
         5),
         


'''
Grupo 6
manos con pardas en 1ra 2da y 3ra:
Hipótesis: manos que si vas en orden son manos de 4 rondas.
'''

    Mano(Ronda(Carta(3, 'B'), Carta(3, 'O')),
         Ronda(Carta(2, 'E'), Carta(2, 'B')),
         Ronda(Carta('R', 'O'), Carta('R', 'C')),
         6),
    Mano(Ronda(Carta(2, 'E'), Carta(2, 'O')),
         Ronda(Carta(2, 'C'), Carta(2, 'B')),
         Ronda(Carta('6', 'O'), Carta('6', 'E')),
         6),
    Mano(Ronda(Carta('R', 'E'), Carta('R', 'C')),
         Ronda(Carta(3, 'C'), Carta(3, 'B')),
         Ronda(Carta('S', 'E'), Carta('S', 'C')),
         6),
    Mano(Ronda(Carta(6, 'B'), Carta(6, 'O')),
         Ronda(Carta('R', 'C'), Carta('R', 'B')),
         Ronda(Carta(4, 'E'), Carta(4, 'O')),
         6),
    Mano(Ronda(Carta(3, 'O'), Carta(3, 'E')),
         Ronda(Carta('C', 'E'), Carta('C', 'B')),
         Ronda(Carta(6, 'B'), Carta(6, 'C')),
         6),


'''
Ojo no voletear el corchete este de acá abajo.
'''
]

