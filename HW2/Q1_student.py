import random
import requests
from myntl import *

API_URL = 'http://cryptlygos.pythonanywhere.com'  # DON'T Change this
my_id = 25083   # CHANGE this into your ID number

# server communication. Try to get p and t
endpoint = '{}/{}/{}'.format(API_URL, "q1", my_id)
response = requests.get(endpoint)
p = 0
t = 0
if response.ok:
    res = response.json()
    print(res)
    # p is your prime number. t is the order of a subgroup. USE THESE TO SOLVE THE QUESTION
    p, t = res['p'], res['t']
else:
    print(response.json())

# SOLUTION
# find the generator of Zp
generators = []
all_possibilities = set(range(1, p))
for chance in all_possibilities:
    check_list = set()
    for validate in all_possibilities:
        check_list.add(pow(chance, validate) % p)
    if check_list == all_possibilities:
        generators.append(chance)
        break


subgroup_generators = []
all_possibilities = set(range(1, p))
for chance in all_possibilities:
    check_list = set()
    for validate in all_possibilities:
        check_list.add(pow(chance, validate) % p)
    if len(check_list) == t:
        subgroup_generators.append(chance)
        break

g = generators[0]           # ATTN: change this into generator you found
gH = subgroup_generators[0] # ATTN: change this into generator of the subgroup you found


# You can CHECK result of PART A here
endpoint = '{}/{}/{}/{}'.format(API_URL, "q1ac", my_id, g)
response = requests.put(endpoint)
print(response.json())


# You can CHECK result of PART B here
# gH is generator of your subgroup
endpoint = '{}/{}/{}/{}'.format(API_URL, "q1bc", my_id, gH)
response = requests.put(endpoint)  # check result
print(response.json())
