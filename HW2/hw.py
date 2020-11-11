from myntl import *
from lfsr import *

# question 3
def linear_congruence(a,b,n):
    solutions = []
    print(gcd(a,n))
    if(b % gcd(a,n) == 0):
        d = gcd(a,n)
        x = (modinv(a//d,n//d)*(b//d)) % (n//d)
        solutions.append(x)
        count = 1
        for i in range(d-1):
            solutions.append(x + count*(n//d))
            count += 1
        return solutions
    else:
        return "NO SOLUTION"

# a
n = 97289040915427312142046186233204893375 
a = 61459853434867593821323745103091100940
b = 22119567361435062372463814709890918083

print(linear_congruence(a,b,n))


#b
n = 97289040915427312142046186233204893375
a = 87467942514366097632147785951765210855 
b = 3291682454206668645932879948693825640

print(linear_congruence(a,b,n))

#c
n = 97289040915427312142046186233204893375 
a = 74945727802091171826938590498744274413 
b = 54949907590247169540755431623509626593

print(linear_congruence(a,b,n))

# question 4
print("***************************Question 4****************************")
import random
length = 256
print ("LFSR: **************")
L = 7
C = [0]*(L+1)
S = [0]*L
    
C[0] = C[2] = C[3] = C[7] = 1 # 1+x+x^7

for i in range(0,L):            # for random initial state
    S[i] = random.randint(0, 1)
print ("Initial state: ", S) 

keystream = [0]*length
for i in range(0,length):
     keystream[i] = LFSR(C, S)
    
print ("First period: ", FindPeriod(keystream))
#print ("L and C(x): ", BM(keystream))
#print ("keystream: ", keystream)


C[0] = C[1] =  C[7] = 1 # 1+x+x^7

for i in range(0,L):            # for random initial state
    S[i] = random.randint(0, 1)
print ("Initial state: ", S) 

keystream = [0]*length
for i in range(0,length):
     keystream[i] = LFSR(C, S)
    
print ("First period: ", FindPeriod(keystream))
#print ("L and C(x): ", BM(keystream))
#print ("keystream: ", keystream)

# question 5
print("***************************Question 5****************************")
x1 = [1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1]
x2 = [0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1]
x3 = [1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0]

print(BM(x1))
print(BM(x2))
print(BM(x3))

# BONUS
print("*************************** BONUS ****************************")
