
import funHttp as h
import simplejson as json

def lista_usuarios(host):
    h.get("http://" + host + ":5371/m2mauth/api/core/user/")
    
def lista_servicios(host,port):
    h.get("http://" + host + ":" + port + "/m2m/v2/services/")

def get_servicio(host, serv_name):
    h.get("http://" + host + ":5371/m2m/v2/services/" + serv_name)


def get_assets(host, serv_name):
    return h.get("http://" + host + ":5371/m2m/v2/services/" + serv_name + "/assets")

def creaDevices(url,lisDevs):
    url = url + '/devices'    
    for dev in lisDevs:
        print dev
        h.post(url, dev)

def borraDevices(url, lista):   
    for dev in lista:
        print dev
        miUrl = url + '/assets/' + dev + '?force=1	'
        print miUrl
        h.delete(miUrl)

# Modelos

def lista_modelos(host,service_name):
    h.get("http://" + host + ":5371/m2m/v2/services/" + service_name + "/models")

def existeModelo(host, service_name, model):            
    return h.get("http://" + host + ":5371/m2m/v2/services/" + service_name + "/models/" + model)
    
	
def creaModelo(url,modeloJson):
    url = url + '/models'    
    h.post(url, modeloJson)
	
def borraModel(url, modelo):            
    miUrl = url + '/models/' + modelo + '?force=1	'
    print miUrl    
        
#envia comando ping
def envio_ping():
    url_cmd = "http://10.95.28.47:8668"
    data ="<paid:command xsi:schemaLocation=\"urn:ogc:def:dictionary:PAID:1.0:paid PaidCommand.xsd\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:swe=\"http://www.opengis.net/swe/1.0.1\" xmlns:paid=\"urn:ogc:def:dictionary:PAID:1.0:paid\" name=\"ping\"></paid:command>"
    post(url_cmd, data)

if __name__ == "__main__":
   # hosts
   INT_DCA22_MC21_HOST = "cloncloud-m2mglobserv01.hi.inet"
   PRODUCCION_HOST = "81.45.14.155"   
   INTEGRACION = "dev-idas-fe-01"

   HOST = INTEGRACION

   # servicio
   SERVICIO = "repsol"

   PORT = "5371"

   print "listar servicios"
   lista_servicios(HOST,PORT)

   print "listar usuarios"
   lista_usuarios(HOST)

   print "servicio " + SERVICIO
   get_servicio(HOST, SERVICIO)

   print "Modelo"
   get_modelos(HOST, SERVICIO)

   print "Assets"
   resp = get_assets(HOST, SERVICIO)
   p = json.loads(resp)
   num_assets = p['count']
   print "numero de assets ", num_assets
   print p['data']
   s = json.loads( p['data'])
   print s
   '''
   for anames in p['data']:
       print anames
       #s = dict(anames)
       
       print s
       #print s['asset']
       p = dict[s['asset']]
       #print p['name']
   '''
