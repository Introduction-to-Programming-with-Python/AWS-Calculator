# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 10:18:16 2021

@author: PCS
"""

import calculadora_aws as calc 

def ejecutar_costo_procesamiento_libre()->None:
    dedicados=int(input("Inserte el numero de servidores dedicados con compromiso: "))
    compartidas=int(input("Inserte el numero de instancias compartidas con compromiso: "))
    costo=float(input("Inserte el costo de un servidor dedicado reservado por una hora: "))
    respuesta=calc.costo_procesamiento_libre(dedicados, compartidas, costo)
    print(respuesta)
    
def iniciar_aplicacion()->None:
    print("Bienvenido al calulador de costo mensual por mantener un número determinado de servidores dedicados y un número determinado de instancias compartidas.")
    ejecutar_costo_procesamiento_libre()
    
iniciar_aplicacion()
