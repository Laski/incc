#!/usr/bin/python2
# -*- coding: utf-8 -*-
import os
import pickle
from scipy.stats import ttest_rel
from matplotlib import pyplot
from tp1 import *

'''
[resultado.preprocesar() for resultado in resultados]
for resultado in resultados:
    with open('resultados/pickle2/'+str(resultado._id), 'wb') as archivo:
        pickle.dump(resultado, archivo, protocol=pickle.HIGHEST_PROTOCOL)

for resultado in resultados:
    print(str(resultado._id) + " " + str(resultado.factor_de_velocidad(resultado.res_exp2)))

for resultado in resultados:
    print(str(resultado._id) + " " + str(resultado.promedios_por_grupo(resultado.res_exp2)))
'''

'''
pyplot.hist(resultados_grupo_control)
pyplot.show()
'''

def ttest_comparativo(resultados, grupo_control, grupo_a_analizar, filtrar=True):
    promedio_por_persona_grupo_control = {}
    promedio_por_persona_grupo_a_analizar = {}
    for resultado in resultados:
        # filtro los individuos que fallaron mas de 3 veces en las pruebas para ver si usaron el algoritmo UCR
        if filtrar and resultado.usa_ucr():
            continue
        try:
            promedio_grupo_control = resultado.promedio_segundo_experimento()[grupo_control]
            promedio_grupo_a_analizar = resultado.promedio_segundo_experimento()[grupo_a_analizar]
        except KeyError:
            # el jugador fallo todas las manos de este grupo
            continue
        promedio_por_persona_grupo_control[resultado._id] = promedio_grupo_control
        promedio_por_persona_grupo_a_analizar[resultado._id] = promedio_grupo_a_analizar

    resultados_grupo_control = []
    resultados_grupo_a_analizar = []
    for persona in promedio_por_persona_grupo_control.keys():
        resultados_grupo_control.append(promedio_por_persona_grupo_control[persona])
        resultados_grupo_a_analizar.append(promedio_por_persona_grupo_a_analizar[persona])

    return ttest_rel(resultados_grupo_control, resultados_grupo_a_analizar)[1]  # p-value

def significancia_grupos_manos(resultados):
    for grupo in range(11):
        if grupo == 3: continue     # no comparo con el mismo
        pvalue =  ttest_comparativo(resultados, 3, grupo, True)
        print(" " + str(grupo) + ": " + (str(pvalue) if pvalue < 0.05 else "NO SIGNIFICATIVO"))

    print("No filtrando a nadie:")
    for grupo in range(11):
        if grupo == 3: continue     # no comparo con el mismo
        pvalue =  ttest_comparativo(resultados, 3, grupo, False)
        print(" " + str(grupo) + ": " + (str(pvalue) if pvalue < 0.05 else "NO SIGNIFICATIVO"))

def correctitud_por_mano(resultados):
    ## TODO
    pass
    

def promedio_por_mano(resultados):
    tiempos = {}
    for resultado in resultados:
        if resultado.usa_ucr():
            continue
        tiempos[resultado._id] = resultado.tiempos_por_ronda(resultado.res_exp2, 0)
    promedios_por_mano = []
    cantidad_sujetos = len(tiempos)
    for num_mano in range(1000):   # me paso, lo voy a cortar antes
        todos = []
        for sujeto in tiempos.keys():
            try:
               todos.append(tiempos[sujeto][num_mano])
            except IndexError:
                # hay un sujeto que no respondió correctamente tantas manos
                # tengo que cortar acá
                return promedios_por_mano
        for i in range(5):
            # tiro outliders
            _max = max(todos)
            todos.remove(_max)
        promedios_por_mano.append(sum(todos) / cantidad_sujetos)
    return promedios_por_mano


def main():
    resultados_nombres = os.listdir('resultados/pickle2')
    archivos = [open('resultados/pickle2/'+filename, 'rb') for filename in resultados_nombres]
    resultados = [pickle.load(archivo) for archivo in archivos]
    [archivo.close() for archivo in archivos]
    significancia_grupos_manos(resultados)
    print(promedio_por_mano(resultados))



main()