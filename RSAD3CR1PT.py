import gmpy
from Crypto.Util.number import *

N = 3247042599234496397528999357195779
E = 65537
c =2770060553560336730843625224405190
P = 56755289255345539
Q = 57211277430476161

phi = (Q-1)*(P-1)


d = gmpy.invert(E,phi)

flag = pow(c,d,N)

print (long_to_bytes(flag))
