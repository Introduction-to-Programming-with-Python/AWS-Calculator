# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 10:18:53 2021

@author: PCS
"""

import calculadora_aws as calc 

def ejecutar_costo_total()->None:
    servidores_compromiso=int(input("Inserte el numero total de maquinas virtuales con compromiso de permanencia: "))
    porcentaje_compartidas_compromiso=float(input("Inserte el porcentaje de instancias que serán compartidas, con compromiso de permanencia: "))
    servidores_libres=int(input("Inserte el número total de máquinas virtuales libres: "))
    porcentaje_compartidas_libres=float(input("Inserte el porcentaje de instancias que serán compartidas, libres: "))
    costo_dedicado=float(input("Inserte el costo por hora de un servidor dedicado: "))
    solicitudes_totales=int(input("Inserte el número de solicitudes totales de lectura y escritura: "))
    almacenamiento=float(input("Inserte el espacio de almacenamiento en GB: "))
    datos=float(input("Inserte la cantidad de datos en GB que se transfieren: "))
    porcentaje_aws=float(input("Inserte el porcentaje de tráfico que se dirige a otros servicios de AWS: "))
    respuesta=calc.costo_total(servidores_compromiso, porcentaje_compartidas_compromiso, servidores_libres, porcentaje_compartidas_libres, costo_dedicado, solicitudes_totales, almacenamiento, datos, porcentaje_aws)
    print(respuesta)
    
def iniciar_aplicacion()->None:
    print("Bienvenido al calulador de costo total.")
    ejecutar_costo_total()
    
iniciar_aplicacion()