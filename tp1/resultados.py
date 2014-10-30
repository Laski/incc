#!/usr/bin/python2
# -*- coding: utf-8 -*-
import os
import pickle
from scipy.stats import ttest_rel, linregress
from matplotlib import pyplot
from tp1 import *

'''
for resultado in resultados:
    print(str(resultado._id) + " " + str(resultado.factor_de_velocidad(resultado.res_exp2)))

for resultado in resultados:
    print(str(resultado._id) + " " + str(resultado.promedios_por_grupo(resultado.res_exp2)))
'''
'''
pyplot.hist(resultados_grupo_control)
pyplot.show()
'''

def ttest_comparativo_tiempo(resultados, grupo_control, grupo_a_analizar, filtrar_dos_rondas):
    promedio_por_persona_grupo_control = {}
    promedio_por_persona_grupo_a_analizar = {}
    for sujeto in resultados:
        try:
            promedio_grupo_control = sujeto.promedio_segundo_experimento(filtrar_dos_rondas=filtrar_dos_rondas)[grupo_control]
            promedio_grupo_a_analizar = sujeto.promedio_segundo_experimento(filtrar_dos_rondas=filtrar_dos_rondas)[grupo_a_analizar]
        except KeyError:
            # el jugador fallo todas las manos de este grupo
            continue
        promedio_por_persona_grupo_control[sujeto._id] = promedio_grupo_control
        promedio_por_persona_grupo_a_analizar[sujeto._id] = promedio_grupo_a_analizar

    resultados_grupo_control = promedio_por_persona_grupo_control.values()
    resultados_grupo_a_analizar = promedio_por_persona_grupo_a_analizar.values()
    if len(resultados_grupo_a_analizar) == 0:
        return
    return ttest_rel(resultados_grupo_control, resultados_grupo_a_analizar)[1]  # p-value


def ttest_comparativo_factor(resultados, grupo_control, grupo_a_analizar, filtrar_dos_rondas):
    factor_por_persona_grupo_control = {}
    factor_por_persona_grupo_a_analizar = {}
    for sujeto in resultados:
        try:
            factor_grupo_control = sujeto.factor_de_velocidad_por_grupo(filtrar_dos_rondas=filtrar_dos_rondas)[grupo_control]
            factor_grupo_a_analizar = sujeto.factor_de_velocidad_por_grupo(filtrar_dos_rondas=filtrar_dos_rondas)[grupo_a_analizar]
        except KeyError:
            # el jugador fallo todas las manos de este grupo
            continue
        factor_por_persona_grupo_control[sujeto._id] = factor_grupo_control
        factor_por_persona_grupo_a_analizar[sujeto._id] = factor_grupo_a_analizar

    resultados_grupo_control = []
    resultados_grupo_a_analizar = []
    for persona in factor_por_persona_grupo_control.keys():
        # para mantener el orden
        resultados_grupo_control.append(factor_por_persona_grupo_control[persona])
        resultados_grupo_a_analizar.append(factor_por_persona_grupo_a_analizar[persona])
    if len(resultados_grupo_a_analizar) == 0:
        # filtrando tanto nos quedamos sin test
        return
    return ttest_rel(resultados_grupo_control, resultados_grupo_a_analizar)[1]  # p-value

def significancia_grupos_manos(resultados, funcion_de_ttest, cant_grupos=11, grupo_control=3, filtrar_dos_rondas=True):
    non_ucr_users = [sujeto for sujeto in resultados if not sujeto.usa_ucr()]
    ucr_users = [sujeto for sujeto in resultados if sujeto.usa_ucr()]

    print("\tNo filtrando a nadie:")
    imprimir_ttest_por_grupo(resultados, cant_grupos, grupo_control, funcion_de_ttest, filtrar_dos_rondas)

    print("\tSolo gente que no usaba UCR (criterio: fallar 3 veces o menos en las pruebas para ver si usaba UCR):")
    imprimir_ttest_por_grupo(non_ucr_users, cant_grupos, grupo_control, funcion_de_ttest, filtrar_dos_rondas)

    print("\tY ahora solo usuarios de UCR:")
    imprimir_ttest_por_grupo(ucr_users, cant_grupos, grupo_control, funcion_de_ttest, filtrar_dos_rondas)
    
def imprimir_ttest_por_grupo(resultados, cant_grupos, grupo_control, funcion_de_ttest, filtrar_dos_rondas):
    for grupo in range(cant_grupos):
        if grupo == grupo_control: continue     # no comparo con el mismo
        pvalue =  funcion_de_ttest(resultados, grupo_control, grupo, filtrar_dos_rondas)
        if pvalue is not None:
            print("\t\t" + str(grupo) + ": " + (str(pvalue) if pvalue < 0.05 else "NO SIGNIFICATIVO"))

def correctitud_por_mano(resultados):
    ## TODO
    pass

def promedio_por_mano(resultados):
    tiempos = {}
    for sujeto in resultados:
        if sujeto.usa_ucr():
            continue
        tiempos[sujeto._id] = sujeto.tiempos_por_ronda(sujeto.res_exp2, 0)
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

def promedio_factores_de_velocidad(resultados):
    factores_de_velocidad_por_grupo = defaultdict(list)
    for sujeto in resultados:
        if sujeto.usa_ucr():
            continue
        factores = sujeto.factor_de_velocidad_por_grupo()
        for grupo in range(11):
            try:
                factores_de_velocidad_por_grupo[grupo].append(factores[grupo])
            except KeyError:
                pass
    promedios = {}
    for grupo in range(11):
        promedios[grupo] = sum(factores_de_velocidad_por_grupo[grupo]) / len(factores_de_velocidad_por_grupo[grupo])
    return promedios

def promedio_tiempos_por_grupo(resultados):
    tiempos_por_grupo = defaultdict(list)
    for sujeto in resultados:
        if sujeto.usa_ucr():
            continue
        tiempos = sujeto.promedio_segundo_experimento()
        for grupo in range(11):
            try:
                tiempos_por_grupo[grupo].append(tiempos[grupo])
            except KeyError:
                pass
    promedios = {}
    for grupo in range(11):
        promedios[grupo] = sum(tiempos_por_grupo[grupo]) / len(tiempos_por_grupo[grupo])
    return promedios

def promedio_primer_tanda(resultados):
    tiempos = []
    for sujeto in resultados:
        tiempos_sujeto = sujeto.promedio_primer_experimento()
        for grupo in range(5):
            try:
                tiempos.append(tiempos_sujeto[grupo])
            except KeyError:
                pass
    return sum(tiempos) / len(tiempos)


def main():
    resultados_nombres = os.listdir('resultados/pickle')
    archivos = [open('resultados/pickle/'+filename, 'rb') for filename in resultados_nombres]
    resultados = [pickle.load(archivo) for archivo in archivos]
    [archivo.close() for archivo in archivos]

    promedios = promedio_tiempos_por_grupo(resultados)
    factores_relevantes = [promedio_primer_tanda(resultados), promedios[2], promedios[3], promedios[5]]
    print(linregress([1, 2, 3, 4], factores_relevantes))

    promedios = promedio_factores_de_velocidad(resultados)
    factores_relevantes = [1, promedios[2], promedios[3], promedios[5]]
    print(linregress([1, 2, 3, 4], factores_relevantes))


    print("SOLO MANOS DE TRES RONDAS")

    print("-Mirando tiempos absolutos")
    significancia_grupos_manos(resultados, ttest_comparativo_tiempo, filtrar_dos_rondas=True)
    print
    print
    print("-Mirando tiempos relativos (tiempo de la mano vs. tiempo promedio por ronda en el primer experimento)")
    significancia_grupos_manos(resultados, ttest_comparativo_factor, filtrar_dos_rondas=True)
    
    print
    print
    print
    print
    
    print("MANOS DE TRES Y DOS RONDAS")

    print("-Mirando tiempos absolutos")
    significancia_grupos_manos(resultados, ttest_comparativo_tiempo, filtrar_dos_rondas=False)
    print
    print
    print("-Mirando tiempos relativos (tiempo de la mano vs. tiempo promedio por ronda en el primer experimento)")
    significancia_grupos_manos(resultados, ttest_comparativo_factor, filtrar_dos_rondas=False)


main()