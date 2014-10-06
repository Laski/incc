 #!/usr/bin/python2
 # -*- coding: utf-8 -*-
VALORES = range(1,8) + ['S', 'C', 'R']
PALOS = ('O', 'C', 'E', 'B')
POSIBLES_GANADORES = IZQUIERDA, DERECHA, PARDA = range(3)
RANDOM = 0


class Carta:
    def __init__(self, valor, palo):
        self.valor = valor
        self.palo = palo
        
    def __str__(self):
        return str(self.valor)+str(self.palo)

    def img_filename(self, dirname):
        if self.palo == 'O':
            palo_str = 'oros'
        elif self.palo == 'C':
            palo_str = 'copas'
        elif self.palo == 'E':
            palo_str = 'espadas'
        elif self.palo == 'B':
            palo_str = 'bastos'
        if self.valor == 'S':
            valor_str = '10'
        elif self.valor == 'C':
            valor_str = '11'
        elif self.valor == 'R':
            valor_str = '12'
        else:
            valor_str = str(self.valor)
        return dirname+'/'+palo_str+'_'+valor_str+'.jpg'

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


CUATROS         = [Carta(4, palo) for palo in PALOS]
CINCOS          = [Carta(5, palo) for palo in PALOS]
SEIS            = [Carta(6, palo) for palo in PALOS]
SIETES_FALSOS   = [Carta(7, 'C'), Carta(7, 'B')]
SOTAS           = [Carta('S', palo) for palo in PALOS]
CABALLOS        = [Carta('C', palo) for palo in PALOS]
REYES           = [Carta('R', palo) for palo in PALOS]
ANCHOS_FALSOS   = [Carta(1, 'O'), Carta(1, 'C')]
DOS             = [Carta(2, palo) for palo in PALOS]
TRES            = [Carta(3, palo) for palo in PALOS]
SIETE_ORO       = [Carta(7, 'O')]
SIETE_ESPADA    = [Carta(7, 'E')]
ANCHO_BASTO     = [Carta(1, 'B')]
ANCHO_ESPADA    = [Carta(1, 'E')]
CARTAS_BAJAS    = [CUATROS, CINCOS, SEIS, SIETES_FALSOS]
CARTAS_MEDIAS   = [SOTAS, CABALLOS, REYES, ANCHOS_FALSOS]
CARTAS_ALTAS    = [DOS, TRES, SIETE_ORO, SIETE_ESPADA, ANCHO_BASTO, ANCHO_ESPADA]
CARTAS_EN_ORDEN = [CUATROS, CINCOS, SEIS, SIETES_FALSOS, SOTAS, CABALLOS, REYES, ANCHOS_FALSOS, DOS, TRES, SIETE_ORO, SIETE_ESPADA, ANCHO_BASTO, ANCHO_ESPADA]


class Mazo:     # hará falta?
    def __init__(self):
        self.cartas = [Carta(valor, palo) for valor in VALORES for palo in PALOS]
        self.cartas.sort(key=lambda carta: carta.fuerza)

    def __str__(self):
        res = ''
        for carta in self.cartas:
            res += str(carta) + '\n'
        return res


class Ronda:
    def __init__(self, carta_izq, carta_der, grupo=0):
        self.carta_izq = carta_izq
        self.carta_der = carta_der
        self.grupo = grupo

    def quien_gana(self):
        if self.carta_izq > self.carta_der:
            return IZQUIERDA
        elif self.carta_der > self.carta_izq:
            return DERECHA
        else:
            return PARDA

    def __str__(self):
        return str(self.carta_izq) + " vs " + str(self.carta_der)
        

class Mano:
    def __init__(self, ronda1, ronda2, ronda3, grupo=0):
        self.rondas = (ronda1, ronda2, ronda3)
        if grupo == 1:
            self.tapar = False
        else:
            self.tapar = True
        self.grupo = grupo
        if self.hay_cartas_repetidas():
            raise ValueError("Hay cartas repetidas")

    def hay_cartas_repetidas(self):
        cartas = [ronda.carta_izq for ronda in self.rondas]
        cartas += [ronda.carta_der for ronda in self.rondas]
        for carta in cartas:
            if cartas.count(carta) > 1:
                return True
        return False

    def quien_gana(self):
        ganador_por_mano = [ganador1, ganador2, ganador3] = [ronda.quien_gana() for ronda in self.rondas]
        for jugador in (IZQUIERDA, DERECHA):
            if ganador_por_mano.count(jugador) >= 2:
                return jugador
        # hubo pardas
        if ganador1 == PARDA:
            if ganador2 == PARDA:
                if ganador3 == PARDA:
                    # las tres fueron pardas, gana mano
                    return IZQUIERDA # izquierda es siempre mano
                else:
                    # parda primera y segunda, gana la tercera
                    return ganador3
            else:
                # parda primera, gana la segunda
                return ganador2
        else:
            # la primera no fue parda pero alguna otra sí, gana primera
            return ganador1

    def tengo_que_tapar_tercera(self):
        if not self.tapar:   # si la mano es patologica se muestran todas las cartas siempre
            return False
        else:
            return self.se_gano_en_la_segunda_ronda()

    def se_gano_en_la_segunda_ronda(self):
        ganador1, ganador2, ganador3 = [ronda.quien_gana() for ronda in self.rondas]
        if ganador1 == ganador2 != PARDA:
            return True
        elif ganador1 == PARDA and ganador2 != PARDA:
            return True
        elif ganador2 == PARDA and ganador1 != PARDA:
            return True
        else:
            return False

    def __str__(self):
        ronda1, ronda2, ronda3 = self.rondas
        return str(ronda1) + ", " + str(ronda2) + ", " + str(ronda3)


def carta_from_string(str):
    pass

def ronda_from_string(str):
    pass

def mano_from_string(str):
    pass

def test():
    for carta in Mazo().cartas:
        assert Carta(1, 'E') > carta or carta == Carta(1, 'E')
        assert Carta(4, 'E') < carta or carta.valor == 4


if __name__ == "__main__":
    test()