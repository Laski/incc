#!/usr/bin/python2
# -*- coding: utf-8 -*-
from psychopy import visual, core, event  # import some libraries from PsychoPy

from cartas import *

# #create a window
# mywin = visual.Window([800,600], monitor="testMonitor", units="deg")

# #create some stimuli
# grating = visual.GratingStim(win=mywin, mask="circle", size=3, pos=[-4,0], sf=3)
# fixation = visual.GratingStim(win=mywin, size=0.5, pos=[0,0], sf=0, rgb=-1)

# #draw the stimuli and update the window
# grating.draw()
# fixation.draw()
# mywin.update()

#pause, so you get a chance to see it!
#core.wait(0.000001)

class Experimento:
    def __init__(self):
        self.mostrador = Mostrador()
    
    def primer_experimento(self, rondas):
        pass
        
    def segundo_experimento(self, manos):
        pass


class Dibujador:
    def __init__(self):
        self.window = visual.Window([1024,768], monitor="testMonitor", units='cm')
        self.x_izq = -4
        self.x_der = 4
        self.y1 = 7
        self.y2 = 12
        self.y3 = 17

    def dibujar_dos(self, imgs_izq_y_der, y=7):
        img_izq, img_der = imgs_izq_y_der
        stim_izq = self.filename_to_stim(img_izq, self.x_izq, y)
        stim_der = self.filename_to_stim(img_der, self.x_der, y)
        stim_izq.draw()
        stim_der.draw()

    def dibujar_seis(self, imgs1y2, imgs3y4, imgs5y6):
        img1, img2 = imgs1y2
        img3, img4 = imgs3y4
        img5, img6 = imgs5y6
        mostrar_dos_cartas(img1, img2, self.y1)
        mostrar_dos_cartas(img3, img4, self.y2)
        mostrar_dos_cartas(img5, img5, self.y3)

    def filename_to_stim(self, filename, x, y):
        return visual.ImageStim(self.window, filename, pos=(x, y))

    def flip(self):
        self.window.flip()


class MostradorCartas:
    def __init__(self, dibujador):
        self.dibujador = dibujador

    def mostrar_mano(self, mano):
        filenames = []
        for ronda in mano.rondas:
            filenames.append(self.ronda_to_filenames(ronda))
        img1y2, img2y3, img5y6 = filenames
        self.dibujador.dibujar_seis(img1y2, img2y3, img5y6)
        self.flip()

    def mostrar_ronda(self, ronda):
        img_izq_y_der = self.ronda_to_filenames(ronda)
        self.dibujador.dibujar_dos(img_izq_y_der)
        self.flip()

    def ronda_to_filenames(self, ronda):
        izq = ronda.carta_izq
        der = ronda.carta_der
        img_izq = izq.img_filename('cartas')
        img_der = der.img_filename('cartas')
        return (img_izq, img_der)

    def flip(self):
        return self.dibujador.flip()


def test():
    dibujador = Dibujador()
    mostrador = MostradorCartas(dibujador)
    carta_izq = ANCHO_ESPADA[0]
    carta_der = ANCHO_BASTO[0]
    ronda = Ronda(carta_izq, carta_der)
    mostrador.mostrar_ronda(ronda)

    clock = core.Clock()
    clock.reset()
    core.wait(3)
    keypresses = event.getKeys(None, clock)
    dibujador.window.close()
    print keypresses

if __name__ == '__main__':
    test()

