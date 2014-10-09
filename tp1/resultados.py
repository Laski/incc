#!/usr/bin/python2
# -*- coding: utf-8 -*-
import os
import pickle
from tp1 import *

resultados_nombres = os.listdir('resultados/pickle')
archivos = [open('resultados/pickle/'+filename, 'rb') for filename in resultados_nombres]
resultados = [pickle.load(archivo) for archivo in archivos]

for resultado in resultados:
    print(str(resultado._id) + " " + str(resultado.factor_de_velocidad(resultado.res_exp2)))

for resultado in resultados:
    print(str(resultado._id) + " " + str(resultado.promedios_por_grupo(resultado.res_exp2)))
