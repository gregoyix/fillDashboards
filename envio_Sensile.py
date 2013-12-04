#from httplib2 import Http


import funHttp as h
import simplejson as json
import time
import datetime
import math
import MetSensile as mm

urlINTEGRACION = 'http://dev-idas-gw-01:8002/repsol/v1'
urlPREPRO = 'http://localhost:8002/repsol/v1' # con el tunel claro

urlIntDCA_MC = 'http://cloncloud-m2mglobserv01.hi.inet:8002/repsol/v1' 

urlPRODUCCION = 'http://81.45.14.155:8002/repsol/v1'

url = urlPREPRO

dic = json.loads('{ "id": "1","from": "","to": "tel:22012;phone-context=+34","timestamp": 1, "message": "" }')
print dic


timestamp = int(time.time()) *1000
print "hora ", timestamp

mes_Nivel_tanque_bajo ="ABCDRM500280712004230C00372A14E1FFFF10FFFFFFFF090105000000010200130110"

mes_Quita_alarma = "ABCDRM50034032100323150011F504B0FFFF33FFFFFFFF09020E000000010200340133"

dic = json.loads('{ "id": "1","from": "","to": "tel:22012;phone-context=+34","timestamp": 1, "message": "" }')
print dic

message = mes_Quita_alarma

dic ['timestamp'] = timestamp
dic ['message'] = message
    
"""

Sensores Sensile

50138187	+34660373185
50139803	+34648420863
50136705	+34659261908
50034032	+34629104701
50097057	+34696207956
50037506	+34636479394

"""

senSensile = [ "+34660373185", "+34648420863", "+34659261908", "+34629104701", "+34696207956", "+34636479394"]

mensaje1 = "i33t0D0913t0000q1Ak1Ab77eC00f0g0h0000c23" # nivel normal de llenado del tanque
mensaje2 = "i33t0D0914t0000q16k17b75e170f0g0h0000c23" # nivel critico de llenado del tanque                         
mensaje3 = "i33t0D0914t0000q16k08b75e170f0g0h0000c23" # nivel temperatura bajo
mensaje4 = "i33t0D0917t0000qAk17b78e800f0g0h0000c23" # bateria por debajo de 9 v
            

#dic ['message'] = mensaje4

print dic ['message']

def envioSensile(sensores, men, niv):
    '''
	sens: sensores a los que se envia el mensaje	
	men: mensaje q se envia
    '''
    for sen in sensores:    
        print sen
        t = 44 # temperatura
        #n = 44  # nivel
        #b battery
        anyo = 13 # anyo
        mes = 12 # mes
        dia = 4 # dia
        dic ['message'] = "i33t" + mm.pasaFecha(str(anyo), str(mes), str(dia)) + "t0900q1A" + mm.codTemp(t) + "b78" + mm.codNivLlenado(niv) + "f0g0h0000c23" 
        dic ['from'] = "tel:" + sen
        data = json.dumps(dic)
        print data
        h.post(url, data)

# Fecha: ????
def envioNativo(sensores, dic):
    for id in sensores:
        dic ['from'] = "tel:" + id        
        data = json.dumps(dic)
        print data
        h.post(url, data)

envioSensile(senSensile,"", 6)


    
'''
def rondaMisiles(dic):
    for id in senSensile:
        dic ['from'] = "tel:" + id        
        data = json.dumps(dic)
        print data
        h.post(url, data)


def ataque():
    t = 16 # temperatura
    n = 0  # nivel
    anyo = 13 # anyo
    mes = 10 # mes
    dia = 11 # dia
    for i in range (0,30):
        dic ['message'] = "i33t" + mm.pasaFecha(str(anyo), str(mes), str(dia)) + "t0900q1A" + mm.codTemp(t) + "b78" + mm.codNivLlenado(n) + "f0g0h0000c23"
        rondaMisiles(dic)
        time.sleep(5) # delays for 5 seconds
        t = (t+3)%100
        n = (n+10)%100
        dia = dia + 1

def ataqueIndiv():
    t = 66 # temperatura
    n = 48  # nivel
    anyo = 13 # anyo
    mes = 9 # mes
    dia = 30 # dia
    dic ['message'] = "i33t" + mm.pasaFecha(str(anyo), str(mes), str(dia)) + "t0900q1A" + mm.codTemp(t) + "b78" + mm.codNivLlenado(n) + "f0g0h0000c23"
    rondaMisiles(dic)
        
#ataque()
#rondaMisiles0(dic)
#ataqueIndiv()

#{ "id": "1","from": "tel:+","to": "tel:638444191;phone-context=+34","timestamp": 1, "message": "i33t0D0904t0000q16k13b7Be800f0g0h0000c23" }
    
t = 66 # temperatura
n = 25  # nivel
anyo = 13 # anyo
mes = 10 # mes
dia = 17 # dia
dic ['message'] = "i33t" + mm.pasaFecha(str(anyo), str(mes), str(dia)) + "t0900q1A" + mm.codTemp(t) + "b78" + mm.codNivLlenado(n) + "f0g0h0000c23"
dic ['from'] = "tel:" +  "+34609876935"        
data = json.dumps(dic)
print data
h.post(url, data)

    
def ataqueHisteresis(n):
    t = 68 # temperatura
    #n = 44  # nivel
    anyo = 13 # anyo
    mes = 10 # mes
    dia = 7 # dia
    dic ['message'] = "i33t" + mm.pasaFecha(str(anyo), str(mes), str(dia)) + "t0900q1A" + mm.codTemp(t) + "b78" + mm.codNivLlenado(n) + "f0g0h0000c23" 
    dic ['from'] = "tel:" + "+34629104701"        
    data = json.dumps(dic)
    print data
    h.post(url, data)

def jimmy(n):
    t = 68 # temperatura
    #n = 44  # nivel
    anyo = 13 # anyo
    mes = 12 # mes
    dia = 1 # dia
    dic ['message'] = "i33t" + mm.pasaFecha(str(anyo), str(mes), str(dia)) + "t0900q1A" + mm.codTemp(t) + "b78" + mm.codNivLlenado(n) + "f0g0h0000c23" 
    dic ['from'] = "tel:" + "+34696207956"        
    data = json.dumps(dic)
    print data
    h.post(url, data)

#dummy609 +34609876935"

#niv = raw_input("Nivel ? ")
#ataqueHisteresis(niv)


#ataque()
#rondaMisiles0(dic)

jimmy(1)

'''
