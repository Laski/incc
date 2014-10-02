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


MANOS_PATOLOGICAS = [
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