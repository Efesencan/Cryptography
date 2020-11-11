import requests
from myntl import *
API_URL = 'http://cryptlygos.pythonanywhere.com'

my_id = 25083

endpoint = '{}/{}/{}'.format(API_URL, "q2", my_id )
response = requests.get(endpoint) 	
if response.ok:	
  r = response.json()
  p, q, e, c = r['p'], r['q'], r['e'], r['cipher']    #Use these variables to calculate m
  print(c)
else:  print(response.json())

##SOLUTION
n = p * q
phi_n = (p-1) * (q-1)
d = modinv(e,phi_n)
c = c % n
d = d % n
calculated_m = pow(c,d,n)
print("calculated m",calculated_m)
## END OF SOLUTION


m = calculated_m 	#ATTN: change this into the number you calculated and DECODE it into a string m_
m_ = calculated_m.to_bytes((calculated_m.bit_length() + 7) // 8, byteorder='big')
m_ = m_.decode("utf-8")
print(m_)
#m_ = "Change this to the message you found from m by decoding. Yes, it is a meaningful text."


#query result
endpoint = '{}/{}/{}/{}'.format(API_URL, "q2c", my_id, m_ )    #send your answer as a string
response = requests.put(endpoint) 	
print(response.json())
