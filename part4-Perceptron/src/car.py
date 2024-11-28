import random

Pb = 0.1
cptR = [1, 0.1]
cptI = [1, 0.05]
Pg = 0.05
cptS = [1, 1, 1, 0.01]
cptM = [1, 0.01]

samples = []
n = 10 ** 5

for _ in range(n):
  B = 1 if random.random() > Pb else 0
  R = 1 if random.random() > cptR[B] else 0
  I = 1 if random.random() > cptI[B] else 0
  G = 1 if random.random() > Pg else 0
  S = 1 if random.random() > cptS[I * 2 + G] else 0
  M = 1 if random.random() > cptM[S] else 0

  samples.append((B, R, I, G, S, M))

print(len(samples))

BRGnegS = 0
RGnegS = 0
SRIG = 0
RIG = 0
SnegRIG = 0
negRIG = 0

for i in range(n):
  B, R, I, G, S, M = samples[i]
  if B and R and G and not S:
    BRGnegS += 1
  if R and G and not S:
    RGnegS += 1
  if S and R and I and G:
    SRIG += 1
  if R and I and G:
    RIG += 1
  if S and not R and I and G:
    SnegRIG += 1
  if not R and I and G:
    negRIG += 1

print("P(B | R,G,¬S) =", BRGnegS / RGnegS)
print("P(S | R,I,G) =", SRIG / RIG)
print("P(S | ¬R,I,G) =", SnegRIG / negRIG)

