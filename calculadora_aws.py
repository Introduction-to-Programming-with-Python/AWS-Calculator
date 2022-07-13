# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 09:21:03 2021

@author: PCS
"""

import calculadora_aws as calc

def tiempo_transferencia(tamaño:float, ancho_banda:int)->str:
    
    """
    
    Realiza el cálculo del tiempo que tardaría la transferencia de varios
    archivos de unos servidores locales a AWS según su tamaño en GB y el ancho
    de banda  medido en Mbps.

    Parameters
    ----------
    
    tamaño : float
        Tamaño total en GB de los archivos a transferir.

    ancho_banda : int
        Ancho de banda en Mbps contratados.

    Returns
    -------
    
    str
        Una cadena que indique el tiempo que tardará en transferirse los
        archivos con el formato "El archivo tardará X horas, Y minutos y Z
        segundos en transferirse".

    """
    #Se pasan los GB a MB y de MB a mb para que quede Mb/Mbps al calcular los segundos
    mb_tamaño=float(tamaño*1024*8)
    #Se calcula el tiempo en segundo mirando, ¿cuantos Mb pasan en el ancho de banda ingresado
    segundos=mb_tamaño/ancho_banda
    
    #Para convertir a formato horas, minutos y segundos. Los segundos se pasan a horas por medio de una division exacta, el resultado son las horas.
    horas_exacta=int(segundos//3600)
    #Se calcula cuantos segundos sobraron en el residuo.
    residuo_segundos=float(segundos%3600)
    #Los segundos sobrantes se convierten a minutos, estos son los minutos.
    minutos=int(residuo_segundos//60)
    #Se calculan los segundos sobrantes de lo anterior, estos son los segundos.
    segundos_restantes=float(segundos%60) 
      
    return str("El archivo tardara " + (str(horas_exacta)) + " horas, " + str(minutos) +" minutos y " + str(segundos_restantes) + " segundos en transferirse.")



def costo_procesamiento_compromiso(dedicados:int, compartidas:int, costo:float)->float:
   
    """

    Calcula el costo mensual de mantener un número determinado de servidores 
    dedicados y un número determinado de instancias compartidas, teniendo en
    cuenta el costo por hora que se cobra por un servidor dedicado.
    Se asume un compromiso de por lo menos 1 año

    Parameters
    ----------
    
    dedicados : int
        Número de servidores dedicados con compromiso que se utilizarán.
    
    compartidas : int
        Número de instancias compartidas con compromiso que se utilizarán.
    
    costo : float:
         Costo de un servidor dedicado reservado por una hora.

    Returns
    -------
    
    float
        Costo total que se tendrá que pagar por el mes de procesamiento con
        compromiso.

    """
    #Se calcula el costo de los servidores dedicados multiplicando el costo por el numero de servidores dedicados, y se eleva a la inversa de 10/9 para sacar la raiz.
    costo_sd=float((costo*dedicados)**(9/10))
    #este es el mismo procedimiento del anterior, solo que con su respectiva raiz y sacando el procentaje de descuento del 10%.
    cost_id=float(((costo*0.9)*compartidas)**(17/20))
    
    #Aca esta la suma de los dos costos, por 720, debido a que el resultado de por si se da en horas y hay que calcularlo por mes.
    resultado=float((cost_id+costo_sd)*720)
    
    return str("El costo mensual de servidores dedicados e instancias compartidas es: " + str(round(resultado,2)))



def costo_procesamiento_libre(dedicados:int, compartidas:int, costo:float)->float:
    
    """
    
    Calcula el costo mensual de mantener un número determinado de
    servidores dedicados y un número determinado de instancias compartidas,
    sin compromiso de permanencia, teniendo en cuenta el costo por hora que
    se cobra por un servidor dedicado.
    
    Parameters
    ----------
    
    dedicados : int
        Número de servidores dedicados libres que se utilizarán.
    
    compartidas : int
        Número de instancias compartidas libres que se utilizarán.
   
    costo : float
        Costo de un servidor dedicado reservado por una hora

    Returns
   -------
    
    float
        Costo total a pagar por el mes de procesamiento libre.

    """
    #Se cacula el costo de los servidores dedicados libres multiplicando su costo por el numero de servidores.
    costo_cd=float(costo*dedicados)
    #Se cacula el costo de los servidores dedicados libres multiplicando su costo(con el descuento aplicado) por el numero de servidores.
    costo_ic=float((costo-(costo*0.10))*compartidas)
    
    resultado=float((costo_cd+costo_ic)*720)
    
    return str("El costo mensual de servidores dedicados e instancias compartidas, sin compromiso de permanencia, es: "+str(round(resultado,2)))



def costo_almacenamiento(lectura:int, escritura:int, almacenamiento:float)->float:
    
    """
    
    Calcula el costo total mensual por almacenamiento en un bucket S3 estándar
    según el número de solicitudes de lectura, solicitudes de escritura y
    tamaño de los datos almacenados en GB.
    
    Parameters
    ----------
    
    lectura : int
        Número de solicitudes de lectura.
    
    ecritura : int
        Número de solicitudes de escritura.
   
    almacenamiento : float:
        Tamaño de la información almacenada en GB.

    Returns
    -------
    
    Float.
        Costo total mensual del bucket.
        
    """
    #Se calcula el costo de las lecturas multiplicando su costo por la razon de sulicitudes de lecturas hechas.
    costo_lectura=float(0.0004*(lectura/1000))
    #Se calcula el costo de las escrituras multiplicando su costo por la razon de escrituras de lecturas hechas.
    costo_escritura=float(0.005*(escritura/1000))
    
    #Se calcula el costo del almacenamiento multiplicando su costo por el numer de GB.
    costo_almacenamiento=float(almacenamiento*0.023)
    
    resultado=round(float(costo_almacenamiento+costo_escritura+costo_lectura),2)
    
    return str("El costo total mensual de almacenamiento es: "+str(resultado))



def costo_transferencia(datos:float, porcentaje_aws:float)->float:
   
    """
    
    Calcula el costo mensual de transferencia de datos, teniendo en cuenta la
    cantidad de datos enviados desde las instancias hacia Internet y hacia
    instancias de AWS en otra región.

    Parameters
    ----------
    
    datos : float
        Cantidad total de datos que se transfirieron en GB.
    
    porcentaje_aws : float
        Porcentaje de los datos que se fueron hacia instancias de AWS en otra
        región. Debe ser un número entre 0 y 1.

    Returns
    -------
    
    float
        Costo total mensual de la transferencia de datos realizada.

    """
    #Se calcula el porcentaje de datos que no se fueron a instancias AWS.
    porcentaje_internet=float(1-porcentaje_aws)
    
    #Teniendo el procentaje, y por medio de una regla de tres, se calcula la cantidad de datos que no se fueron a instancias AWS.
    cant_internet=float((porcentaje_internet*datos)/1)
    #Teniendo el procentaje, y por medio de una regla de tres, se calcula la cantidad de datos qe se fueron a instancias AWS.
    cant_aws=float((porcentaje_aws*datos)/1)
    
    #Se calcula el costo de la transferencia de datos que no se fueron a instancias AWS, restando 1 a la cantidad de datos, esto por ser el primer GB gratis por mes.
    costo_transferencia_internet=float((cant_internet-1)*0.09)
    #Se calcula el costo de la transferencia de datos que se fueron a instancias AWS.
    costo_transferencia_aws=float(cant_aws*0.02)
    resultado=round((float(costo_transferencia_aws+costo_transferencia_internet)),2)
    
    return str("El costo mensual de transferencia de datos es :"+str(resultado))

#ESTA NO ME DIO, LE HICE DE TODO Y NADA :( Igual ahi esta el procedimineto y creo que esta bien solo que no supe enlazar las funciones

def costo_total(servidores_compromiso:int, porcentaje_compartidas_compromiso:
                float, servidores_libres:int, porcentaje_compartidas_libres:
                float, costo_dedicado:float, solicitudes_totales:int,
                almacenamiento:float, datos:float, porcentaje_aws:float)->str:
   
    """
    
    Costo mensual de contratar una infraestructura que incluye procesamiento,
    almacenamiento y transferencia de datos. Para las solicitudes de
    transferencia se asume que 1/3 corresponden a escritura (si obtiene una
    cantidad decimal con esta fracción, aproxímela al entero más cercano)

    Parameters
    ----------
    
    servidores_compromiso : int
        Número total de máquinas virtuales (servidores dedicados e instancias
        compartidas), con compromiso de permanencia.
    
    porcentaje_compartidas_compromiso : float
        Porcentaje de instancias que serán compartidas, con compromiso de
        permanencia. Si al calcular el número de instancias compartidas con
        este porcentaje resulta un número decimal, la cantidad debe
        aproximarse al entero más cercano.
    
    servidores _libres : int
        Número total de máquinas virtuales (servidores dedicados e instancias
        compartidas) libres.
    
    porcentaje_compartidas_libres : float
        Porcentaje de instancias que serán compartidas, libres. Si al calcular
        el número de instancias compartidas con este porcentaje resultad un
        número decimal, la cantidad debe aproximarse al entero más cercano.
    
    costo_dedicado : float
        Costo por hora de un servidor dedicado.
    
    solicitudes_totales : int
        Número de solicitudes totales de lectura y escritura.
    
    almacenamiento : float
        Espacio de almacenamiento en GB.
    
    datos : float
        Cantidad de datos en GB que se transfieren.
    
    porcentaje_aws : float
        Porcentaje de tráfico que se dirige a otros servicios de AWS.

    Returns
    -------
    
    str
        Costo mensual aproximado con el formato “El costo total mensual de
        mantener la infraestructura en AWS es $X USD” donde X es el costo
        total mensual de la infraestructura, en dólares.

    """
    #Calculo de costo por los servidores con compromiso
    
def ejecutar_costo_procesamiento_compromiso()->None:
#Se calcula el procentaje de instancias dedicadas con compromiso, sabiendo que 1 es el 100% y el porcentaje a calcular es la diferencia entre el 100% y el porcentaje ya dado.(el de instancias compartidas con compromiso)
porcentaje_dedicadas_compromiso=1-porcentaje_compartidas_compromiso
#Ya sabiendo los porcentajes de cada tipo de maquina virtual con compromiso, se sacan la cantidad de cada una sabiendo la cantidad total de servidores con compromiso, por medio de una regla de tres.
servidores_dedicados=(porcentaje_dedicadas_compromiso*servidores_compromiso)/1
#Se hace el mismo procedimiento anterior, pero ahora para calcular la cantidad de instancias compartidas.
servidores_compartidas=(porcentaje_compartidas_compromiso*servidores_compromiso)/1
costo_procesamiento_compromiso(servidores_dedicados, servidores_compartidas, costo_dedicado)

#Calculo de costo por los servidores libres
    
def ejecutar_costo_procesamiento_libre()->None:
#Se calcula el procentaje de instancias dedicadas libres, sabiendo que 1 es el 100% y el porcentaje a calcular es la diferencia entre el 100% y el porcentaje ya dado.(el de instancias compartidas con compromiso)
porcentaje_dedicados_libres=1-porcentaje_compartidas_libres
#Ya sabiendo los porcentajes de cada tipo de maquina virtual libre, se sacan la cantidad de cada una sabiendo la cantidad total de servidores libres, por medio de una regla de tres.
#Se hace el mismo procedimiento anterior, pero ahora para calcular la cantidad de instancias compartidas.
servidores_compartidas=(porcentaje_compartidas_libres*servidores_libres)/1
servidores_dedicados=(porcentaje_dedicados_libres*servidores_libres)/1
costo_procesamiento_libre(servidores_dedicados, servidores_compartidas, costo_dedicado)
    
#Calculo de solicitudes totales
    
def ejecutar_costo_almacenamiento()->None:
#Se calculan las solicitudes de escritura, asumiendo que estas son 1/3 de lassolicitudes totales.
solicitudes_escritura=solicitudes_totales*1/3
#Se calculas las solicitudes de lectura, siendo estas la procion restantes.
solicitudes_lectura=solicitudes_totales-solicitudes_escritura
costo_almacenamiento(solicitudes_lectura, solicitudes_escritura, almacenamiento)
    
#costo_transferencia
    
def ejecutar_costo_transferencia()->None:
costo_transferencia(datos, porcentaje_aws)
    

    
return "El costo mensual de mantener la infraestructura en AWS es $"+str(costo)+" USD."



