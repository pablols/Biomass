# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 23:08:20 2016

@author: Pablo
"""

import numpy as np
import codecs
import json
import urllib
import time



datos=np.genfromtxt('datos.txt', dtype=['|S5',float,'|S5','|S5','|S5','|S5',float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,float], skip_header=1, delimiter=';')


n_datos=len(datos)



url_1='https://maps.googleapis.com/maps/api/directions/json?'
url_2='&lenguage=es&units=metric&Mode=driving'

api_key1='your_api_key'








#LOOP CON EL CUAL SE OBTIENE LOS ARCHIVOS .JSON OBTENIDOS DESDE LA GOOGLE MAPS DIRECTIONS API
for i in range(0,n_datos):
    print(i) 
    xi='origin='+str(datos[i][10])+','+str(datos[i][9])
    xf='&destination='+str(datos[i][21])+','+str(datos[i][20])
    xixf=str(datos[i][10])+','+str(datos[i][9])+'  ;  '+str(datos[i][21])+','+str(datos[i][20])
    qry=url_1+xi+xf+url_2+api_key1
    response = urllib.urlopen(qry)
    data = json.loads(response.read())
    data1 = json.dumps(data, sort_keys = True, ensure_ascii=False)
    with codecs.open('JSON_'+str(xixf)+'.txt', 'w', 'utf8') as f:
        f.write(data1)
    f.close
    time.sleep(.3) 

print ('fin')