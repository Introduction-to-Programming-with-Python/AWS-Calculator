# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 10:18:35 2021

@author: PCS
"""

import calculadora_aws as calc 

def ejecutar_costo_transferencia()->None:
    datos=float(input("Inserte la cantidad total de datos que se transfirieron en GB: "))
    porcentaje_aws=float(input("Inserte el porcentaje de los datos que se fueron hacia instancias de AWS en otra región: "))
    respuesta=calc.costo_transferencia(datos, porcentaje_aws)
    print(respuesta)
    
def iniciar_aplicacion()->None:
    print("Bienvenido al calulador de costo mensual por transferencia de datos.")
    ejecutar_costo_transferencia()
    
iniciar_aplicacion()