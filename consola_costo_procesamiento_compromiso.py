# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 10:17:59 2021

@author: PCS
"""
import calculadora_aws as calc

def ejecutar_costo_procesamiento_compromiso()->None:
    dedicados=int(input("Inserte el numero de servidores dedicados con compromiso: "))
    compartidas=int(input("Inserte el numero de instancias compartidas con compromiso: "))
    costo=float(input("Inserte el costo de un servidor dedicado reservado por una hora: "))
    resultado=calc.costo_procesamiento_compromiso(dedicados, compartidas, costo)
    print(resultado)
    
def iniciar_aplicacion()->None:
    print("Bienvenido al calulador de costo mensual por mantener un número determinado de servidores dedicados y un número determinado de instancias compartidas.")
    ejecutar_costo_procesamiento_compromiso()
    
iniciar_aplicacion()