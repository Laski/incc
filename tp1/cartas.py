 # -*- coding: utf-8 -*-
VALORES = range(1,8) + ['S', 'C', 'R']
PALOS = ['O', 'C', 'E', 'B']
POSIBLES_GANADORES = IZQUIERDA, DERECHA, PARDA = range(3)
CUATROS = [Carta(4, palo) for palo in PALOS]
CINCOS = [Carta(5, palo) for palo in PALOS]
SEIS = [Carta(6, palo) for palo in PALOS]
SIETES_FALSOS = [[Carta(7, 'C'), Carta(7, 'B')]]
SOTAS = [Carta('S', palo) for palo in PALOS]
CABALLOS = [Carta('C', palo) for palo in PALOS]
REYES = [Carta('R', palo) for palo in PALOS]
ANCHOS_FALSOS = [Carta(1, 'O'), Carta(1, 'C')]
DOS = [Carta(2, palo) for palo in PALOS]
TRES = [Carta(3, palo) for palo in PALOS]
SIETE_ORO = [Carta(7, 'O')]
SIETE_ESPADA = [Carta(7, 'E')]
ANCHO_BASTO = [Carta(1, 'B')]
ANCHO_ESPADA = [Carta(1, 'E')]
CARTAS_EN_ORDEN = [CUATROS, CINCOS, SEIS, SIETES_FALSOS, SOTAS, CABALLOS, REYES, ANCHOS_FALSOS, DOS, TRES, SIETE_ORO, SIETE_ESPADA, ANCHO_BASTO, ANCHO_ESPADA]


class Carta:
    def __init__(self, valor, palo):
        self.valor = valor
        self.palo = palo
        
    def __str__(self):
        return str(valor)+str(palo)
    
    @property
    def img_filename(self, dirname):
        return dirname+str(self)

    @property
    def fuerza(self):
        # devuelve un entero que indica la fuerza de la carta. cuanto mayor es, más fuerte es
        for fuerza in range(len(CARTAS_EN_ORDEN)):
            if self in CARTAS_EN_ORDEN[fuerza]:
                return fuerza
        raise ValueError("No soy una carta válida")

      # las cartas son comparables
    def __eq__(self, other):
        return self.valor == other.valor and self.palo == other.palo
    def __ne__(self, other):
        return not self == other
    def __gt__(self, other):
        return other < self
    def __ge__(self, other):
        return not self < other
    def __le__(self, other):
        return not other < self
    def __lt__(self, other):  # caso base
        return self.fuerza < other.fuerza


class Mazo:
    def __init__(self):
        self.cartas = [Carta(valor, palo) for valor in VALORES for palo in PALOS]


class Ronda:
    def __init__(self, carta_izq, carta_der):
        self.carta_izq = carta_izq
        self.carta_der = carta_der

    def quien_gana():
        if self.carta_izq > self.carta_der:
            return IZQUIERDA
        elif self.carta_der > self.carta_izq:
            return DERECHA
        else:
            return PARDA


class Mano:
    def __init__(self, ronda1, ronda2, ronda3):
        self.ronda1 = ronda1
        self.ronda2 = ronda2
        self.ronda3 = ronda3
        self.rondas = (ronda1, ronda2, ronda3)

    def quien_gana(self):
        for jugador in (IZQUIERDA, DERECHA):
            if self.rondas_ganadas_por(jugador) >= 2:
                return jugador
        # hubo pardas
        ganador1 = ronda1.quien_gana()
        ganador2 = ronda2.quien_gana()
        ganador3 = ronda3.quien_gana()
        if ganador1 == PARDA:
            if ganador2 == PARDA:
                if ganador3 == PARDA:
                    return IZQUIERDA # izquierda es siempre mano
                else:
                    return ganador3
            else:
                return ganador2
        else:
            return ganador1

    def rondas_ganadas_por(self, jugador):
        return len([None for ronda in self.rondas if ronda.quien_gana() == jugador])