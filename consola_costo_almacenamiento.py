# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 10:18:25 2021

@author: PCS
"""

import calculadora_aws as calc 

def ejecutar_costo_almacenamiento()->None:
    lectura=int(input("Inserte la cantidad de lecturas hechas al mes: "))
    escritura=int(input("Inserte la cantidad de escrituras hechas al mes: "))
    almacenamiento=float(input("Inserte la cantidad de almacenamiento: "))
    resultado=calc.costo_almacenamiento(lectura, escritura, almacenamiento)
    print(resultado)
    
def iniciar_aplicacion()->None:
    print("Bienvenido al calulador de costo mensual por almacenamiento.")
    ejecutar_costo_almacenamiento()
    
iniciar_aplicacion()