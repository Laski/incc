#!/usr/bin/python2
# -*- coding: utf-8 -*-
import random
from psychopy import visual, core, event  # import some libraries from PsychoPy
from cartas import *
from casos_patologicos import *

INCORRECTO, CORRECTO = range(2)

VERDE = [25.0/255*2-1, 77.0/255*2-1, 30.0/255*2-1]    # los pajeros estos van de -1 a 1

class Experimento:
    def __init__(self):
        self.mostrador = Mostrador()
    
    def primer_experimento(self, rondas):
        pass
        
    def segundo_experimento(self, manos):
        pass


class Dibujador:
    def __init__(self):
        #self.window = visual.Window([1024,768], monitor="testMonitor", units='cm', color=VERDE)
        self.window = visual.Window(fullscr=True, monitor="testMonitor", units='cm', color=VERDE)
        self.x_izq = -4
        self.x_der = 4
        self.y1 = 5
        self.y2 = 0
        self.y3 = -5
        self.y_unica = 0

    def dibujar_dos(self, imgs_izq_y_der, y=None):
        y = self.y_unica if y is None else y
        img_izq, img_der = imgs_izq_y_der
        stim_izq = self.filename_to_stim(img_izq, self.x_izq, y)
        stim_der = self.filename_to_stim(img_der, self.x_der, y)
        stim_izq.draw()
        stim_der.draw()

    def dibujar_seis(self, imgs1y2, imgs3y4, imgs5y6):
        self.dibujar_dos(imgs1y2, self.y1)
        self.dibujar_dos(imgs3y4, self.y2)
        self.dibujar_dos(imgs5y6, self.y3)

    def mostrar_tick(self):
        stim = self.filename_to_stim('tick.png', 0, 0)
        stim.draw()
        self.flip()
        core.wait(0.1)

    def mostrar_cross(self):
        stim = self.filename_to_stim('cross.png', 0, 0)
        stim.draw()
        self.flip()
        core.wait(0.1)

    def filename_to_stim(self, filename, x, y):
        return visual.ImageStim(self.window, filename, pos=(x, y))

    def flip(self):
        self.window.flip()


class MostradorCartas:
    def __init__(self):
        self.dibujador = Dibujador()
        self.dorso = 'cartas/dorso.jpg'

    def mostrar_mano(self, mano):
        filenames = []
        ronda1, ronda2, ronda3 = mano.rondas
        for ronda in mano.rondas:
            filenames.append(self.ronda_to_filenames(ronda))
        img1y2, img2y3, img5y6 = filenames
        if mano.tengo_que_tapar_tercera():
            img5y6 = (self.dorso, self.dorso)
        self.dibujador.dibujar_seis(img1y2, img2y3, img5y6)
        self.flip()

    def mostrar_ronda(self, ronda):
        img_izq_y_der = self.ronda_to_filenames(ronda)
        self.dibujador.dibujar_dos(img_izq_y_der)
        self.flip()

    def mostrar(self, cartas):
        if isinstance(cartas, Mano):
            self.mostrar_mano(cartas)
        else:
            self.mostrar_ronda(cartas)

    def mostrar_dorsos(self, cant):
        par = (self.dorso, self.dorso)
        if cant == 2:
            self.dibujador.dibujar_dos(par)
        elif cant == 6:
            self.dibujador.dibujar_seis(par, par, par)
        self.dibujador.flip()
        event.waitKeys()

    def ronda_to_filenames(self, ronda):
        izq = ronda.carta_izq
        der = ronda.carta_der
        img_izq = izq.img_filename('cartas')
        img_der = der.img_filename('cartas')
        return (img_izq, img_der)

    def mostrar_tick(self):
        self.dibujador.mostrar_tick()

    def mostrar_cross(self):
        self.dibujador.mostrar_cross()

    def flip(self):
        return self.dibujador.flip()


class Experimento:
    def __init__(self):
        self.mostrador = MostradorCartas()
        self.mazo = Mazo()
        self.clock = core.Clock()

    def mostrar_y_tomar_tiempo(self, cartas):
        ganador = cartas.quien_gana()
        self.mostrador.mostrar(cartas)
        self.clock.reset()
        key, time = event.waitKeys(keyList=('left', 'right'), timeStamped=self.clock)[0]
        if (key == 'left' and ganador == IZQUIERDA) or (key == 'right' and ganador == DERECHA):
            self.mostrador.mostrar_tick()
            return CORRECTO, cartas.grupo, str(cartas), time
        else:
            self.mostrador.mostrar_cross()
            return INCORRECTO, cartas.grupo, str(cartas), time

    def cartas_al_azar(self, cant):
        todas = self.mazo.cartas[:]
        res = []
        for i in range(cant):
            carta = random.choice(todas)
            if cant == 2:
                todas = [carta2 for carta2 in todas if carta2.fuerza != carta.fuerza]    # no muestro pardas
            else:
                todas.remove(carta)
            res.append(carta)
        return res

    def varias_al_azar(self, cant):
        resultados = []
        for i in range(cant):
            resultados.append(self.mostrar_al_azar())
        return resultados

    def mostrar_dorsos(self):
        self.mostrador.mostrar_dorsos(self.cant)

    def mostrar_al_azar(self):
        ''' Abstracto '''
        raise NotImplemented("Mostrar al azar")

    def descanso(self):
        self.mostrar_dorsos()

    def ejecutar(self, cant_tandas, tests_por_tanda, instancias_especificas):
        resultados = []
        tandas = []
        primer_tanda = [self.cartas_al_azar() for i in(tests_por_tanda)]
        tandas.append(primer_tanda)     # la primer tanda no tiene instancias especificas
        instancias_faltantes = (cant_tandas-1)*tests_por_tanda+instancias_especificas
        for i in range(instancias_faltantes):
            instancias = 
        for tanda in tandas:
            self.descanso()
            resultados += self.varias_al_azar(tests_por_tanda)
            resultados.append("Descanso")
        print(resultados)        


class Experimento1(Experimento):
    def __init__(self):
        Experimento.__init__(self)
        self.cant = 2

    def ronda_al_azar(self):
        izq, der = self.cartas_al_azar(2)
        return Ronda(izq, der)

    def mostrar_al_azar(self):
        ronda = self.ronda_al_azar()
        return self.mostrar_y_tomar_tiempo(ronda)
    

class Experimento2(Experimento):
    def __init__(self):
        Experimento.__init__(self)
        self.cant = 6

    def mano_al_azar(self):
        izq1, der1, izq2, der2, izq3, der3 = self.cartas_al_azar(self.cant)
        ronda1, ronda2, ronda3 = Ronda(izq1, der1), Ronda(izq2, der2), Ronda(izq3, der3)
        return Mano(ronda1, ronda2, ronda3)

    def mostrar_al_azar(self):
        mano = self.mano_al_azar()
        return self.mostrar_y_tomar_tiempo(mano)

def exp1(rondas_especificas):
    exp = Experimento1()
    exp.ejecutar(4, 1, rondas_especificas)
    
def exp2(manos_especificas):
    exp = Experimento2()
    exp.ejecutar(4, 1, manos_especificas)


if __name__ == '__main__':
    exp1(RONDAS_PATOLOGICAS)
    exp2(MANOS_PATOLOGICAS)

