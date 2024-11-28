import random

pE = 110/111
pB = 364/365
cptA = [1-0.0095, 1-0.92, 1-0.81, 1-0.97]

samples = []
n = 10 ** 5

for _ in range(n):
  E = 1 if random.random() > pE else 0
  B = 1 if random.random() > pB else 0
  A = 1 if random.random() > cptA[E * 2 + B] else 0

  samples.append((E, B, A))

print(len(samples))

BA = 0
BAE = 0
Ap = 0
AE = 0

for i in range(n):
  E, B, A = samples[i]
  if B and A:
    BA += 1
  if B and A and E:
    BAE += 1
  if A:
    Ap += 1
  if A and E:
    AE += 1

print("P(B | A) =", BA / Ap)
print("P(B | A, E) =", BAE / AE)

#  Give an interpretation to your answers for items 1 & 2. What probabilities do they approximate? 
# They approximate P(B | A) and P(B | A, E).
# Are they in line with your intuition? In other words, do they make sense? In particular: which of the fractions is bigger and why? 
# P(B | A) is bigger than P(B | A, E). 
