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






