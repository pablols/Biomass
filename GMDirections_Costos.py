# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 23:48:49 2015

@author: Pablo
"""
import numpy as np
import json




datos=np.genfromtxt('datos_r.txt', dtype=['|S5',float,'|S5','|S5','|S5','|S5',float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,float], skip_header=1, delimiter=';')
n_datos=len(datos)


cont_ok=0
cont_zr=0

resultados=np.zeros((n_datos,10))


#LECTURA DE ARCHIVOS JSON PARA TODO LOS BOSQUES DE LA VII REGION
for i in range(0,n_datos):
    ix=99999999999999       #asumo valores iniciales arbitrariamente altos para resaltar errores al correr el codigo
    iy=99999999999999       #asumo valores iniciales arbitrariamente altos para resaltar errores al correr el codigo
    fx=99999999999999       #asumo valores iniciales arbitrariamente altos para resaltar errores al correr el codigo
    fy=99999999999999       #asumo valores iniciales arbitrariamente altos para resaltar errores al correr el codigo
    d=99999999999999        #asumo valores iniciales arbitrariamente altos para resaltar errores al correr el codigo
    t=99999999999999        #asumo valores iniciales arbitrariamente altos para resaltar errores al correr el codigo
    print(str(i*100/n_datos)+'%')
    name_i='JSON_'+str(datos[i][10])+','+str(datos[i][9])+'  ;  '+str(datos[i][21])+','+str(datos[i][20])+'.txt'
    response = open(name_i,"r")
    data = json.loads(response.read())
    if data['status']=='OK':
        cont_ok=cont_ok+1
        ix=data['routes'][0]['legs'][0]['start_location']['lng']
        iy=data['routes'][0]['legs'][0]['start_location']['lat']
        fx=data['routes'][0]['legs'][0]['end_location']['lng']
        fy=data['routes'][0]['legs'][0]['end_location']['lat']
        d=data['routes'][0]['legs'][0]['distance']['value']
        t=data['routes'][0]['legs'][0]['duration']['value']
    if data['status']=='ZERO_RESULTS':
        cont_zr=cont_zr+1
        ix=0
        iy=0
        fx=0
        fy=0
        d=0
        t=0
    resultados[i,0]=datos[i][9]   #coordenadas x del predio i
    resultados[i,1]=datos[i][10]      #coordenadas y del predio i
    resultados[i,2]=datos[i][20]    #coordenadas x del centro de oferta asocaido al predio i
    resultados[i,3]=datos[i][21]    #coordenadas y del centro de oferta asociado al predio j
    resultados[i,4]=ix              #coordenada x asociada a la calle de partida mas cercana al predio i
    resultados[i,5]=iy              #coordenada y asociada a la calle de partida mas cercana al predio i
    resultados[i,6]=fx              #coordenada x asociada a la calle de partida mas cercana al centro de oferta del predio i
    resultados[i,7]=fy              #coordenada y asociada a la calle de partida mas cercana al centro de oferta del predio i
    resultados[i,8]=d               #distancia del recorrido
    resultados[i,9]=t               #tiempo estimado en realizar el recorrido

if (cont_ok+cont_zr)/n_datos==1:
    print('--------------FIN_OK-------------')
else:
    ('--------------FIN_ERROR-------------')