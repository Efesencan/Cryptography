from lfsr import *

import itertools

print("*******************Question 4*******************")
# correlation attack
#generate all possible initial states for C1
initial_states = list(itertools.product([0, 1], repeat=14))
C1 = [1,0,0,0,0,1,0,0,0,0,0,0,0,0,1]
z = [0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1]
correlation_check = dict()
max_count = 0
maxLfsr_a = []
max_produced_sequence_a = []
for i in initial_states:
    if i != [0]*14:
        count = 0
        Lista = list(i)
        store_Lista = Lista.copy()
        produced_sequence_a = []
        for j in z:
            a = LFSR(C1,Lista)
            if a == j:
                count += 1
            produced_sequence_a.append(a)
        if count > max_count:
            max_count = count
            maxLfsr_a = store_Lista
            max_produced_sequence_a = produced_sequence_a
        produced_sequence_a = []

print(max_count/len(z))

# correlation attack for C2 (it has the less correlation ratio)
# initial_states = list(itertools.product([0, 1], repeat=17))
# correlation_check = []
# C2 = [1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
# for i in initial_states:
#     if list(i) != [0]*17:
#         count = 0
#         Listb = list(i)
#         for j in z:
#             if LFSR(C2,Listb) == j:
#                 count += 1
#         correlation_check.append(count/len(z))

# print(max(correlation_check))

# correlation attack for C3
initial_states = list(itertools.product([0, 1], repeat=11))
correlation_check = dict()
C3 = [1,0,1,0,0,0,0,0,0,0,0,1]
max_count = 0
maxLfsr_c = []
max_produced_sequence_c = []
for i in initial_states:
    if list(i) != [0]*11:
        count = 0
        Listc = list(i)
        store_Listc = Listc.copy()
        produced_sequence_c = []
        for j in z:
            c = LFSR(C3,Listc)
            if  c == j:
                count += 1
            produced_sequence_c.append(c)
        if count > max_count:
            max_count = count
            maxLfsr_c = store_Listc
            max_produced_sequence_c = produced_sequence_c
        produced_sequence_c = []


print(max_count/len(z))

# find inital state of LFSR2
initial_states = list(itertools.product([0, 1], repeat=17))
correlation_check = []
C2 = [1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
for i in initial_states:
    if list(i) != [0]*17:
        Listb = list(i)
        store_Listb = Listb.copy()
        check = 1
        for j in range(len(z)):
            x1 = max_produced_sequence_a[j]
            x2 = LFSR(C2,Listb)
            x3 = max_produced_sequence_c[j]
            output = (x1 & x2) ^ (x2 & x3) ^ (x3)
            if output != z[j]:
                check = 0
        if check:
            print("Initial state of LFSR1:",maxLfsr_a)
            print("Initial state of LFSR2:",store_Listb)
            print("Initial state of LFSR3:",maxLfsr_c)
            break

    


    


