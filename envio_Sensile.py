#from httplib2 import Http


import funHttp as h
import simplejson as json
import time
import datetime
import math
import metSensile as mm
import ConfigParser



'''
Leo opciones de configuracion
'''
config = ConfigParser.RawConfigParser()
config.read('confEnvioRepsol.cfg')

print "##################################"
# Obtengo el entorno y la url de envio
print "Entorno > ", config.get('Entorno', 'entorno')
url = config.get('Entorno', 'url')
print "url -> ", url
print "##################################"
# Obtengo la fecha y el numero de medidas que se envia al dia
dia = config.getint('Fecha', 'dia')
print "dia -> ", dia
mes = config.getint('Fecha', 'mes')
print "mes -> ", mes
anyo = config.getint('Fecha', 'anyo')
print "anyo -> ", anyo
medidasAlDia = config.getint('Fecha', 'medidasAlDia')
print "medidasAlDia -> ", medidasAlDia
print "##################################"
# Obtengo los valores iniciales de las variables
try:
       temp = config.getint('Variables', 'tempo')
except ConfigParser.NoOptionError:
       temp = 0
print "temperatura inicial -> ", temp
try:
       niv = config.getint('Variables', 'niv')
except ConfigParser.NoOptionError:
       niv = 0
print "nivel de llenado -> ", niv
try:
       bat = config.getint('Variables', 'bat')
except ConfigParser.NoOptionError:
       bat = 0
print "bateria -> ", bat
print "##################################"

dic = json.loads('{ "id": "1","from": "","to": "tel:22012;phone-context=+34","timestamp": 1, "message": "" }')
print dic


timestamp = int(time.time()) *1000
print "hora ", timestamp

dic = json.loads('{ "id": "1","from": "","to": "tel:22012;phone-context=+34","timestamp": 1, "message": "" }')
print dic


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

#envioSensile(senSensile,"", 6)


    
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
