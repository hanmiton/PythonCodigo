#function mod symmetric

from __future__ import division

def quot(z, p):
        # http://stackoverflow.com/questions/3950372/round-with-integer-division
        return (z + p // 2) // p
        
def mod(z, p):
        return z - quot(z,p) * p
	

#normal symmetric scheme

import random
import math
import pdb 

#pdb.set_trace()
LAMBDA = 16 #security parameter
N = LAMBDA	
P = LAMBDA ** 2
Q = LAMBDA ** 5

def keygen(n):
	key = random.getrandbits(P)
	while(key % 2 == 0):
		key = random.getrandbits(P)
	return key

def encrypt(key, aBit):
	q = random.getrandbits(Q)
	m_a = 2 * random.getrandbits(N - 1)
	c = key * q + m_a + aBit
	return c

def decrypt(key, cipherText):
	return mod(cipherText, key) % 2

def add(cipherText1, cipherText2):
	return cipherText1 + cipherText2

def mult(cipherText1, cipherText2):
	return cipherText1 * cipherText2

def bin(numero):
	binario = ""
	listaN = []
	listaRn = []
	if (numero >0):
		while (numero >0):
			if(numero%2 ==0):
				listaN.append(0)
				binario="0"+binario
			else:
				listaN.append(1)
				binario = "1"+ binario
			numero = int (math.floor(numero/2))
	else:
		if (numero ==0):
			listaN.append(0)
			return listaN
		else:
			return " no se pudo convertir el numero. ingrese solo numeros positivos"	
	for i in reversed(listaN):
		listaRn.append(i)
	return listaRn


#print key
m1 = int (raw_input("ingrese un numero positivo\n"))
m2 = int (raw_input("ingrese un numero positivo\n"))
boln1 = bin(m1)
boln2 = bin(m2)
boln1Encrypt = []
boln2Encrypt = []
sumEncrypt = []
mulEnctypt = []
res = []
aux = []

if(len(boln1) > len(boln2)):
	print len(boln1) - len(boln2)
	for i in range(0, len(boln1) - len(boln2)):
		aux.append(0)
	boln2 = aux + boln2
else:
	print len(boln2) - len(boln1)
	for i in range(0, len(boln2) - len(boln1)):
		aux.append(0)
	boln1 = aux + boln1

key = map(keygen,boln1)
print boln1
print boln2

boln1Encrypt = map(encrypt,key,boln1)
print boln1Encrypt
boln2Encrypt = map(encrypt,key,boln2)
sumEncrypt = map(add,boln1Encrypt,boln2Encrypt)
#print sumEncrypt
mulEnctypt = map(mult,boln1Encrypt, boln2Encrypt)
resSuma = map (decrypt, key, sumEncrypt)
print resSuma
strSuma = ''.join(str(e) for e in resSuma)
resMult = map (decrypt, key, mulEnctypt)
#print resMult
strMult = ''.join(str(e) for e in resMult)
print int(strSuma, 2)
#
"""

c_add = add(c1, c2)
c_mult = mult(c1, c2)
print "c_add = ", c_add
print "c_mult = ", c_mult
c_add_mult = add(c_add, c_mult)
c_mult_mult = mult(c_add, c_mult)

p_add = decrypt(key, c_add)
p_mult = decrypt(key, c_mult)
p_add_mult = decrypt(key, c_add_mult)
p_mult_mult = decrypt(key, c_mult_mult)

print "m1 + m2", p_add
print "m1 * m2", p_mult
print "(m1 + m2) + (m1 * m2)", p_add_mult
print "(m1 + m2) * (m1 * m2)", p_mult_mult
"""