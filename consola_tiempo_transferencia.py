# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 10:18:45 2021

@author: PCS
"""

import calculadora_aws as calc

def ejecutar_tiempo_transferencia()->None:
    tamaño=float(input("Inserte el tamaño total en GB de los archivos a transferir: "))
    ancho_banda=int(input("Inserte el ancho de banda en Mbps contratados: "))
    resultado=calc.tiempo_transferencia(tamaño, ancho_banda)
    print(resultado)
    
def iniciar_aplicacion()->None:
    print("Bienvenido al calulador de tiempo de transferencia.")
    ejecutar_tiempo_transferencia()
    
iniciar_aplicacion()
