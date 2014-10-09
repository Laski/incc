#!/usr/bin/python2
# -*- coding: utf-8 -*-
import os
import pickle
from tp1 import *

resultados_nombres = os.listdir('resultados/pickle')
archivos = [open('resultados/pickle/'+filename, 'rb') for filename in resultados_nombres]
resultados = [pickle.load(archivo) for archivo in archivos]

for resultado in resultados:
    print(resultado.promedio_segunda_tanda(resultado.res_exp1))