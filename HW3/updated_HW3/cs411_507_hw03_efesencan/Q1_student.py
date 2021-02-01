import random
import requests
import BitVector
#from pyfinite import ffield
from gf256 import GF256

API_URL = 'http://cryptlygos.pythonanywhere.com'	#DON'T CHANGE THIS
my_id = 25083 									#ATTN: Change this into your id number

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


n = 8
modulus = BitVector.BitVector(bitstring = '100011011') # irreducible polynom 
bit_a = BitVector.BitVector(bitstring = a)
bit_b = BitVector.BitVector(bitstring = b)
c = bit_a.gf_multiply_modular(bit_b, modulus, n)
a_inv = bit_a.gf_MI(modulus, n)

# integer_a = 0
# count = len(a) - 1
# for i in range(len(a)):
#   integer_a += pow(2,count) * int(a[i])
#   count -=1

# integer_b = 0
# count = len(b) - 1
# for i in range(len(b)):
#   integer_b += pow(2,count) * int(b[i])
#   count -=1

# c = GF256(integer_a) * GF256(integer_b)
# c = '01110011'

# a_inv = GF256(1) / GF256(integer_a)
# a_inv = '10100000'


##END OF SOLUTION
 
#check result of part a

endpoint = '{}/{}/{}/{}'.format(API_URL, "mult", my_id, c)
response = requests.put(endpoint) 	
print(response.json())

#check result of part b
endpoint = '{}/{}/{}/{}'.format(API_URL, "inv", my_id, a_inv)
response = requests.put(endpoint) 	
print(response.json())
