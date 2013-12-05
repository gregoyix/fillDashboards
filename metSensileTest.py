
"""
Unit test for metSensile.py

"""

__author__ = "Gregorio Martin (gregoyix@gmail.com)"
__version__ = "$Revision: 1.0 $"
__date__ = "$Date: 2013/12/12 17:05:20 $"
__copyright__ = "Copyright (c) 2013 Gregorio Martin"
__license__ = "Python"

import metSensile
import unittest

class Miexp_rapida(unittest.TestCase):

    def test33a(self):
        a =  gmpy.mpz(3)  
        b =  gmpy.mpz(3)  
        result = funcGMPY.miexp_rapida(a, b, 45)
        self.assertEqual(27, result)

    def PRUcodTemp():
    try:
       temp = raw_input("Temperatura ? ")
       print "Temperatura " + codTemp(int(temp))
    except ValueError:
       print "Eso no es un numero"		
    def test33b(self):
        a =  gmpy.mpz(3)
        b =  gmpy.mpz(3)
        result = funcGMPY.miexp_rapida(a, b, 12)
        self.assertEqual(3, result)

class Exp_rapida(unittest.TestCase):

    def test33a(self):
        a =  gmpy.mpz(3)
        b =  gmpy.mpz(3)
        result = funcGMPY.exp_rapida(a, b, 45)
        self.assertEqual(27, result)

    def test33b(self):
        a =  gmpy.mpz(3)
        b =  gmpy.mpz(3)
        result = funcGMPY.exp_rapida(a, b, 12)
        self.assertEqual(3, result)

if __name__ == "__main__":
    unittest.main()
