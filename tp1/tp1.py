#!/usr/bin/python2
# -*- coding: utf-8 -*-
from psychopy import visual, core, event  # import some libraries from PsychoPy

import cartas

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


class Mostrador:
    def __init__(self):
        self.window = visual.Window([1024,768], monitor="testMonitor", units='cm')
        #self.window = visual.Window(fullscr=True, monitor="testMonitor", units='cm')


    def imprimir_cartas(imgs1y2, imgs3y4, imgs5y6):
        #imprime las cartas en orden en window
        img1, img2 = imgs1y2
        img3, img4 = imgs3y4
        img5, img6 = imgs5y6


def test():
    mostrador = Mostrador()

    izq = visual.ImageStim(mostrador.window, 'cartas/bastos_1.jpg', pos=(-4, 7) )
    der = visual.ImageStim(mostrador.window, 'cartas/espadas_1.jpg', pos=(4, 7) )
    izq.draw()
    der.draw()
    clock = core.Clock()
    mostrador.window.flip()
    clock.reset()
    core.wait(3)

    keypresses = event.getKeys(None,clock)
    #mostrador.imprimir_cartas(par1, par2, par3)
    mostrador.window.close()
    print keypresses

test()

