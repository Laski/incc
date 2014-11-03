#!/usr/bin/python2
# -*- coding: utf-8 -*-
import os
import pickle
from scipy.stats import ttest_rel, linregress
from matplotlib import pyplot
from tp1 import *


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
    return ttest_rel(resultados_grupo_control, resultados_grupo_a_analizar)


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
    return ttest_rel(resultados_grupo_control, resultados_grupo_a_analizar)


def significancia_grupos_manos(resultados, funcion_de_ttest, cant_grupos=10, grupo_control=3, filtrar_dos_rondas=True):
    non_ucr_users = [sujeto for sujeto in resultados if not sujeto.usa_ucr()]
    ucr_users = [sujeto for sujeto in resultados if sujeto.usa_ucr()]

    print("\tNo filtrando a nadie:")
    imprimir_ttest_por_grupo(resultados, cant_grupos, grupo_control, funcion_de_ttest, filtrar_dos_rondas)

    print("\tSolo gente que no usaba UCR (criterio: fallar 3 veces o menos en las pruebas para ver si usaba UCR):")
    imprimir_ttest_por_grupo(non_ucr_users, cant_grupos, grupo_control, funcion_de_ttest, filtrar_dos_rondas)

    print("\tY ahora solo usuarios de UCR:")
    imprimir_ttest_por_grupo(ucr_users, cant_grupos, grupo_control, funcion_de_ttest, filtrar_dos_rondas)
    

def imprimir_ttest_por_grupo(resultados, cant_grupos, grupo_control, funcion_de_ttest, filtrar_dos_rondas):
    for grupo in range(cant_grupos+1):
        if grupo == grupo_control: continue     # no comparo con el mismo
        res_ttest = funcion_de_ttest(resultados, grupo_control, grupo, filtrar_dos_rondas)
        if res_ttest is not None:
            print("\t\t" + str(grupo) + ": "),
            if res_ttest[1] > 0.05:
                print("NO SIGNIFICATIVO: \t" + str(res_ttest[1]))
            else:
                print(("MÁS RÁPIDO: \t\t" if res_ttest[0] > 0 else "MÁS LENTO: \t\t\t") + str(res_ttest[1]))


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

def plotear_promedio_por_mano(resultados):
    tiempos = promedio_por_mano(resultados)
    pyplot.clf()
    pyplot.plot(tiempos)
    pyplot.xlabel(u"Número de mano")
    pyplot.ylabel("Tiempo de respuesta (segundos)")
    pyplot.savefig("informe/tiempo_por_mano")


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


def tiempos_totales(resultados, grupo, filtrar_ucr, solo_ucr, filtrar_dos_rondas):
    res = []
    for sujeto in resultados:
        if filtrar_ucr and sujeto.usa_ucr():
            continue
        if solo_ucr and not sujeto.usa_ucr():
            continue
        res += sujeto.tiempos_segundo_experimento(filtrar_dos_rondas)[grupo]
    return res

def histogramas_comparativos(resultados, grupo_1, grupo_2=3, solo_ucr=False, filtrar_ucr=True, filtrar_dos_rondas=True):
    if solo_ucr: filtrar_ucr = False
    tiempos_grupo_1 = tiempos_totales(resultados, grupo_1, filtrar_ucr, solo_ucr,  filtrar_dos_rondas)
    tiempos_grupo_2 = tiempos_totales(resultados, grupo_2, filtrar_ucr, solo_ucr, filtrar_dos_rondas)

    bins = [i*0.25 for i in range(60)] if not solo_ucr else [i*0.1 for i in range(50)]

    pyplot.clf()
    pyplot.hist(tiempos_grupo_1, bins=bins, alpha=1, label="Grupo de test", normed=True, color='r')
    pyplot.hist(tiempos_grupo_2, bins=bins, alpha=0.5, label="Grupo control", normed=True, color='b')
    pyplot.legend(loc='upper right')
    pyplot.xlabel("Tiempo de respuesta (segundos)")
    pyplot.savefig("informe/"+str(grupo_1)+"vs"+str(grupo_2)+("ucr" if solo_ucr else ""))

def regresion_lineal(y):
    x = [1, 2, 3, 4]
    slope, intercept, r_value, p_value, std_err = linregress(x, y)
    print(linregress(x, y))
    line = slope*x+intercept
    pyplot.clf()
    pyplot.plot(x, line, 'r-', x, y, 'bo-')
    pyplot.ylabel("Tiempo de respuesta (segundos)")
    pyplot.xlabel("Cantidad de rondas a mirar (estimada)")
    pyplot.savefig("informe/lineal")    


def main():
    resultados_nombres = os.listdir('resultados/pickle')
    archivos = [open('resultados/pickle/'+filename, 'rb') for filename in resultados_nombres]
    resultados = [pickle.load(archivo) for archivo in archivos]
    [archivo.close() for archivo in archivos]

    plotear_promedio_por_mano(resultados)
    histogramas_comparativos(resultados, 2, 3, filtrar_dos_rondas=False)
    histogramas_comparativos(resultados, 5, 3)
    histogramas_comparativos(resultados, 10, 3)
    histogramas_comparativos(resultados, 5, 3, solo_ucr=True)
    histogramas_comparativos(resultados, 6, 3, solo_ucr=True)


    promedios = promedio_tiempos_por_grupo(resultados)
    factores_relevantes = [promedio_primer_tanda(resultados), promedios[2], promedios[3], promedios[5]]
    regresion_lineal(factores_relevantes)


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