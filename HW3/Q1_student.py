import random
import requests
import BitVector
#from lfsr import *

API_URL = 'http://cryptlygos.pythonanywhere.com'	#DON'T CHANGE THIS
my_id = 25083								#ATTN: Change this into your id number

endpoint = '{}/{}/{}'.format(API_URL, "poly", my_id )
response = requests.get(endpoint) 	
a = 0
b = 0
if response.ok:	
  res = response.json()
  print(res)
  a, b = res['a'], res['b']		#Binary polynomials a and b
else:
  print(response.json())

##SOLUTION  
from functools import reduce

# constants used in the multGF2 function
mask1 = mask2 = polyred = None

def setGF2(degree, irPoly):
    """Define parameters of binary finite field GF(2^m)/g(x)
       - degree: extension degree of binary field
       - irPoly: coefficients of irreducible polynomial g(x)
    """
    def i2P(sInt):
        """Convert an integer into a polynomial"""
        return [(sInt >> i) & 1
                for i in reversed(range(sInt.bit_length()))]    
    
    global mask1, mask2, polyred
    mask1 = mask2 = 1 << degree
    mask2 -= 1
    polyred = reduce(lambda x, y: (x << 1) + y, i2P(irPoly)[1:])
        
def multGF2(p1, p2):
    """Multiply two polynomials in GF(2^m)/g(x)"""
    p = 0
    while p2:
        if p2 & 1:
            p ^= p1
        p1 <<= 1
        if p1 & mask1:
            p1 ^= polyred
        p2 >>= 1
    return p & mask2

    
# Define binary field GF(2^8)/x^8 + x^4 + x^3 + x + 1
# (used in the Advanced Encryption Standard-AES)
setGF2(8, 0b100011011)

c = '0' + str(bin(multGF2(0b11111011, 0b01000111))[2:])
print(c)
a_inv = ""
#You need to calculate c and a_inv
#c = a(x)*b(x)
#a_inv is inverse of a

##END OF SOLUTION
 

#check result of part a
endpoint = '{}/{}/{}/{}'.format(API_URL, "mult", my_id, c)
response = requests.put(endpoint) 	
print(response.json())

# #check result of part b
# endpoint = '{}/{}/{}/{}'.format(API_URL, "inv", my_id, a_inv)
# response = requests.put(endpoint) 	
# print(response.json())
