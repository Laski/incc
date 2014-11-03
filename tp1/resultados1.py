#!/usr/bin/python2
# -*- coding: utf-8 -*-
import os
import pickle
from scipy.stats import ttest_rel, linregress
from matplotlib import pyplot
from tp1 import *


def ttest_comparativo_tiempo(resultados, grupo_control, grupo_a_analizar):
    promedio_por_persona_grupo_control = {}
    promedio_por_persona_grupo_a_analizar = {}
    for sujeto in resultados:
        try:
            promedio_grupo_control = sujeto.promedio_primer_experimento()[grupo_control]
            promedio_grupo_a_analizar = sujeto.promedio_primer_experimento()[grupo_a_analizar]
        except KeyError:
            # el jugador fallo todas las manos de este grupo
            continue
        promedio_por_persona_grupo_control[sujeto._id] = promedio_grupo_control
        promedio_por_persona_grupo_a_analizar[sujeto._id] = promedio_grupo_a_analizar

    resultados_grupo_control = promedio_por_persona_grupo_control.values()
    resultados_grupo_a_analizar = promedio_por_persona_grupo_a_analizar.values()
    if len(resultados_grupo_a_analizar) == 0:
        return
    return ttest_rel(resultados_grupo_control, resultados_grupo_a_analizar)


def significancia_grupos_manos(resultados, funcion_de_ttest, cant_grupos=4):
    imprimir_ttest_por_grupo(resultados, cant_grupos, 5, funcion_de_ttest)


def imprimir_ttest_por_grupo(resultados, cant_grupos, grupo_control, funcion_de_ttest):
    for grupo in range(cant_grupos+1):
        if grupo == grupo_control: continue     # no comparo con el mismo
        res_ttest = funcion_de_ttest(resultados, grupo_control, grupo)
        if res_ttest is not None:
            print("\t\t" + str(grupo) + ": "),
            if res_ttest[1] > 0.05:
                print("NO SIGNIFICATIVO: \t" + str(res_ttest[1]))
            else:
                print(("MÁS RÁPIDO: \t\t" if res_ttest[0] > 0 else "MÁS LENTO: \t\t\t") + str(res_ttest[1]))

def tiempos_totales(resultados, grupo):
    res = []
    for sujeto in resultados:
        res += sujeto.tiempos_primer_experimento()[grupo]
    return res


def histogramas_comparativos(resultados, grupo_1, grupo_2=5):
    tiempos_grupo_1 = tiempos_totales(resultados, grupo_1)
    tiempos_grupo_2 = tiempos_totales(resultados, grupo_2)

    bins = [i*0.1 for i in range(50)]

    pyplot.clf()
    pyplot.hist(tiempos_grupo_1, bins=bins, alpha=1, label="Grupo de test", normed=True, color='r')
    pyplot.hist(tiempos_grupo_2, bins=bins, alpha=0.5, label="Grupo control", normed=True, color='b')
    pyplot.legend(loc='upper right')
    pyplot.xlabel("Tiempo de respuesta (segundos)")
    pyplot.ylabel("Cantidad de respuestas (normalizado)")
    pyplot.savefig("informe/rondas"+str(grupo_1)+"vs"+str(grupo_2))

def promedio_por_ronda(resultados):
    tiempos = {}
    for sujeto in resultados:
        tiempos[sujeto._id] = sujeto.tiempos_por_ronda(sujeto.res_exp1, 0)
    promedios_por_ronda = []
    cantidad_sujetos = len(tiempos)
    for num_ronda in range(1000):   # me paso, lo voy a cortar antes
        todos = []
        for sujeto in tiempos.keys():
            try:
               todos.append(tiempos[sujeto][num_ronda])
            except IndexError:
                # hay un sujeto que no respondió correctamente tantas manos
                # tengo que cortar acá
                return promedios_por_ronda
        for i in range(5):
            # tiro outliders
            _max = max(todos)
            todos.remove(_max)
        promedios_por_ronda.append(sum(todos) / cantidad_sujetos)
    return promedios_por_ronda

def plotear_promedio_por_ronda(resultados):
    tiempos = promedio_por_ronda(resultados)
    pyplot.clf()
    pyplot.plot(tiempos)
    pyplot.xlabel(u"Número de ronda")
    pyplot.ylabel("Tiempo de respuesta (segundos)")
    pyplot.savefig("informe/tiempo_por_ronda")

def main():
    resultados_nombres = os.listdir('resultados/pickle')
    archivos = [open('resultados/pickle/'+filename, 'rb') for filename in resultados_nombres]
    resultados = [pickle.load(archivo) for archivo in archivos]
    [archivo.close() for archivo in archivos]
    
    plotear_promedio_por_ronda(resultados)
    histogramas_comparativos(resultados, 1, 5)
    histogramas_comparativos(resultados, 3, 5)
    histogramas_comparativos(resultados, 4, 5)

    significancia_grupos_manos(resultados, ttest_comparativo_tiempo, cant_grupos=7)

main()