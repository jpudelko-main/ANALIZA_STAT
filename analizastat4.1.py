#### zestaw 5 przedzialy ufnosci 
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from math import sqrt
import scipy.stats as stats
## zadanie 2 zestaw 5
alpha = 0.01
z = stats.norm.ppf(1-alpha/2, 0, 1)
srednia = 125

n = 130
s = 15
delta = z*s/sqrt(n)
print (z)
print(delta)
przedzial = (srednia - delta,srednia + delta)
print(przedzial)
### zadanie 3
n3 = 15
srednia3 = 119
s = 2.1
alpha = 0.01
#a)
df = n3 - 1
t = stats.t.ppf(1-alpha/2,df)
delta3  = t*s/sqrt(n3)
przedzial3 = (srednia3 -delta3, srednia3 + delta3)
print(t)
print(srednia3)
print(przedzial3)
#zadanie 4
n4 = 136
#75 PACJENTOW CHOROBY SERCA
r = 75
p1 = r/n4
alfa = 0.05
z4 = stats.norm.ppf(1-alfa/2)
print(z4)
print(p1)
delta4 = z4 *sqrt(p1 * (1-p1) / n4)
print(delta4)
przedzial4 = (p1-delta4, p1+delta4)
print(przedzial4)
#zadanie 5
alfa5 = 0.05
s5 = 15
d5 = 2
z5 = stats.norm.ppf(1-alfa5/2)
n = (z5*s5/d5)**2
print(z5)
print(n)
### zadanie 6
p6 = 0.5
alfa6 = 0.05
z6 = stats.norm.ppf(1-alfa6/2)
d6 = 0.05
n = z6**2 * p6*(1-p6) / d6**2
print(z6)
print(n)
### zadanie 1 zestaw zadan 6
#zalozenie proba pochodzi z populacji o rozkladzie normalnm 
sredniaaaa = 27
alfa1 = 0.05
n1 = 10
df = n1 - 1
s1 = 5
t1 = stats.t.ppf(1-alfa1/2,df)
delta1  = t1*s1/sqrt(n1)
print(t1)
print(delta1)
przedzial11 = (sredniaaaa-delta1,sredniaaaa+delta1)
print(przedzial11)
#nie ma powodu do odrzucenia h0