#!/usr/bin/python2
# -*- coding: utf-8 -*-
from psychopy import visual, core  # import some libraries from PsychoPy

import cartas

#create a window
mywin = visual.Window([800,600], monitor="testMonitor", units="deg")

#create some stimuli
grating = visual.GratingStim(win=mywin, mask="circle", size=3, pos=[-4,0], sf=3)
fixation = visual.GratingStim(win=mywin, size=0.5, pos=[0,0], sf=0, rgb=-1)

#draw the stimuli and update the window
grating.draw()
fixation.draw()
mywin.update()

#pause, so you get a chance to see it!
#core.wait(0.000001)

class Experimento:
    def __init__(self):
        self.mostrador = Mostrador()
    
    def primer_experimento(self, rondas):
        pass
        
    def segundo_experimento(self, manos):
        pass


class Mostrador:
    def __init__(self):
        self.window = visual.Window([800,600], monitor="testMonitor", units="deg")

    def imprimir_cartas(imgs1y2, imgs3y4, imgs5y6):
        #imprime las cartas en orden en window
        img1, img2 = imgs1y2
        img3, img4 = imgs3y4
        img5, img6 = imgs5y6


def test():
    mostrador = Mostrador()
    par1 = ("cartas/5O.jpg", "cartas/6O.jpg")
    par2 = ("cartas/5O.jpg", "cartas/6O.jpg")
    par3 = ("cartas/5O.jpg", "cartas/6O.jpg")
    mostrador.print_cards(par1, par2, par3)

test()

