# use "pip install pyprimes" if pyprimes is not installed
# use "pip install pycryptodome" if pycryptodome is not installed
import math
import random
import sympy
import requests

API_URL = 'http://cryptlygos.pythonanywhere.com'

my_id = 25083   #Change this to your ID

endpoint = '{}/{}/{}'.format(API_URL, "RSA_OAEP", my_id )   
response = requests.get(endpoint) 	
c, N, e = 0,0,0 
if response.ok:	
  res = response.json()
  print(res)
  c, N, e = res['c'], res['N'], res['e']    ##get c, N, e
else: print(response.json())

########

from RSA_OAEP import *
from RSA_OAEP_client import *

PIN_ = 0
for i in range(1000,10000):
    for r in range(2**(k0-1), 2**k0-1):
        isC = RSA_OAEP_Enc(i, e, N, r)
        if isC == c:
          PIN_ = r
          break
    break


#  
########

# Client sends PIN_ to server
endpoint = '{}/{}/{}/{}'.format(API_URL, "RSA_OAEP", my_id, PIN_)
response = requests.put(endpoint)
print(response.json())