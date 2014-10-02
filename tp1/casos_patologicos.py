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
GRUPO (-1, -1, -1): Sin clasificar.
GRUPO (x, y, z):
    x:
        0: manos de 2 o 3 rondas tapando las no jugadas
        1: manos de 3 rondas donde la mano termino en la segunda, y la tercera ronda la ganó el que ganó la mano 
        2: manos de 3 rondas donde la mano termino en la segunda, y la tercera ronda la ganó el que perdió la mano  <== GRUPO 1
    y:
        0: sin pardas
        1: con parda en la primera o la segunda
        2: con parda en la tercera
        3: parda en todas

        Pardas:
            0 0 1 -> 2 
            1 1 0 -> 2
            1 1 1 -> 3
    z:
        0: no peleada (grupos distintos)
        1: una mano peleada (cartas enfrentadas del mismo grupo)
        2: varias manos peleadas (cartas enfrentadas del mismo grupo)
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

]