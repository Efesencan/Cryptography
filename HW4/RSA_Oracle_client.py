import random
import requests
from sympy import *

API_URL = 'http://cryptlygos.pythonanywhere.com'

my_id = 25083   ## Change this to your ID

endpoint = '{}/{}/{}'.format(API_URL, "RSA_Oracle", my_id )
response = requests.get(endpoint) 	
c, N, e = 0,0,0 
if response.ok:	
  res = response.json()
  print(res)
  c, N, e = res['c'], res['N'], res['e']    #get c, N, e
else: print(response.json())

######

r = 5 # define random integer
c_ =  c * pow(r,e,N)

###### Query Oracle it will return corresponding plaintext
endpoint = '{}/{}/{}/{}'.format(API_URL, "RSA_Oracle_query", my_id, c_)
response = requests.get(endpoint) 	
if(response.ok): m_ = (response.json()['m_'])
else:print(response)

####
print("m_:",m_)
res = (m_ * mod_inverse(r,N)) % N
res = res.to_bytes((res.bit_length() + 7) // 8, byteorder='big')
###Send your answer to the server.
endpoint = '{}/{}/{}/{}'.format(API_URL, "RSA_Oracle_checker", my_id, res)
response = requests.put(endpoint)
print(response.json())