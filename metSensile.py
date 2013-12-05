
import datetime

"""

Metodos para codificar observaciones de Sensile

"""

# Temperatura
# Se codifica en hexadecimal

def codTemp(t):
    if t < 0:
       return 'k00'
    elif t > 255:
       return 'kFF'
    else:
       return 'k' + format(t, '02X')
    
def PRUcodTemp():
    try:
       temp = raw_input("Temperatura ? ")
       print "Temperatura " + codTemp(int(temp))
    except ValueError:
       print "Eso no es un numero"

# nivel de llenado
# Se codifica en hexadecimal N*4096/100)

def codNivLlenado(n):
    if n < 0:
       return 'e000'
    elif n >= 100:
       return 'efff'
    else:
       return 'e' + format(n*4096/100, '03X')

def PRUcodNivLlenado():
    try:
       nivel = raw_input("Nivel de llenado ? ")
       print "Nivel de llenado " + codNivLlenado(int(nivel))
    except ValueError:
       print "Eso no es un numero"

# Fecha
# Se codifica en hexadecimal tAAMMDD 0D091B

def codFecha(fecha):
    #1/11/2012
    ss = datetime.datetime.strptime(fecha, '%m/%d/%Y')
    an = ss.strftime('%y')
    anST = format(int(an), '02X')
    mes = ss.strftime('%m')
    mesST = format(int(mes), '02X')
    dia = ss.strftime('%d')
    diaST = format(int(dia), '02X')
    return anST + mesST + diaST

def pasaFecha(anyo, mes, dia):
    return codFecha( mes + "/"  + dia + "/20" + anyo )
   
def PRUcodFecha():
       anyo = raw_input("Anyo ? ")
       mes = raw_input("Mes ? ")
       dia = raw_input("Dia ? ")
       print "Fecha " + pasaFecha(anyo, mes, dia)
   

if __name__ == "__main__":
    #PRUcodTemp()
    #PRUcodNivLlenado()
    PRUcodFecha()
