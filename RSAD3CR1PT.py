# -*- coding: utf-8 -*-
import gmpy
import binascii
from fractions import gcd
#---------------------------------------------------
#colhendo dados

p = int(input("Digite o valor de P:"))
q = int(input("Digite o valor de Q:"))
N = p*q
M = int(input("Digite a mensagem (em decimal):"))
e = int(input("Digite um número primo:"))

phi = (p-1)*(q-1)

#---------------------------------------------------
#achando o valor de D
assert gcd(e, phi) == 1

d = gmpy.invert(e, phi)

assert d != 0

#---------------------------------------------------
#descobrindo a frase encriptada e decriptada

C = pow(M, e, N)
K = pow(C, d, N)

print ('Mensagem:', M)
print ('Chave privada e chave publica:', e, d)
print ('Mensagem Encriptada e Mensagem Decriptada:', C, K)

assert K == M



