import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# zadanie 1 zestaw 6
srednia = 27
s = 5
n = 10
df = n-1
alpha = 0.05
mu0 = 30
from math import sqrt
#funkcja testowa t 
t = (srednia - mu0)/ s*sqrt(n)
print(t)
import scipy.stats as stats
#wartosc krytyczna
wk = stats.t.ppf(1-alpha/2,df)
print(wk)
#obszar krytyczny (-niesk,-2.26> U <2,26,+niesk)
#t nie lezy w obszarze krytycznym , nie mamy podstaw do odrzucenia H0
n = 12
abst = abs(t)
p = 2*(1 - stats.t.cdf(abst,df))
print(p)
#zadanie 2 zestaw 6
n2 = 12
alfa2 = 0.05
#h0 mi =165 mm Hg
#Ha mi <165 mm Hg
#zalozenie : proba pochodzi z populacji o rozkladzie normalnym
import statistics as st
dane  = [183, 152, 178, 157, 194, 163, 144, 114, 178, 152, 118, 158]
srednia2 = st.mean(dane)
print(srednia2)
s2 = st.stdev(dane)
print(s2)
# TEST 1 FUNKCJA TESTOWA POTRRZEBUJEMY = T,TALFA ,N-1
# mi0 == srednia dla populacji === w tym przypadku H0
mi0= 165
df2 = n-1
t2 = (srednia2 - mi0)/ s2 * sqrt(n)
wk2 = stats.t.ppf(1-alfa2,df2)
print(t2)
print(wk2)
# T nie lezy w obszarze krytycznym nie ma podstaw do odrzucenia H0
#obszar krytyczny (-nieskonczonosc, -1,8>
#Postepowanie 2 prawdopodobienstwo statystyczne 
import scipy.stats as stats
p2 = stats.t.cdf(t2,df2)
print(p2)
stats.ttest_1samp(dane,popmean = 165)
mediana2 = np.median(dane)
print(mediana2)
skosnosc2 = stats.skew(dane)
print(skosnosc2)
plt.hist(dane)
plt.show()
#zadanie 3 
#H0 mi=122 cm 
#HA mi=/= 122cm
#ZADANIE 4 
#H0 mi = 30 lat
#hA mi <30 lat
#duza proba bo wiecej niz 30 os 
#test lewostronny 
#brak zalozen dotyczacych rozkladu normalnego bo duza proba 
n = 50
alfa4 = 0.05
mi04 = 30 
zgony = pd.read_excel(r"C:\Users\jpude\OneDrive\Pulpit\rzeczy do python anal.stat\Zgony (1).xlsx")
print(zgony)
srednia4 = zgony["Wiek"].mean()
print(srednia4)
mediana4 = zgony["Wiek"].median()
print(mediana4)
s4 = zgony["Wiek"].std()
print(s4)
plt.hist(zgony)
plt.show()
Z = (srednia4 - mi04) / s4 * sqrt(n)
print(Z)
#wartosc krytyczna
wk4 = stats.norm.ppf(1-alfa4)
print(wk4)
#obszar krytyczny (-nieskoncz,-1,64> Z lezy w obszarze krytyczntym (-4.18) odrzucamy hipoteze 0
#dodatkowo oblicz wartosc p (prawdopodobienstwo stat)
p4 = stats.norm.cdf(Z)
print(p4)
print(stats.ttest_1samp(zgony["Wiek"],popmean = 30))
#p = 0.00011 < alfa ==> odrzucamy h0 (test dwustronnny)
### ZADANIE 5 LISTA 6
# H0 = p==0.05
# Ha = p<0.05 # test lewostronny 
alfa5 = 0.05 #poziom istotnosci### cale zadanie slajd 32 wyklad 9
p05 = 0.05
r5 = 18
n = 423
phat5 = 18/423
print(phat5)
z5 = (phat5 - p05) / sqrt(p05 *(1-p05)/n)

print(z5)
zalfa = stats.norm.ppf(1-alfa5)
print(zalfa)
#obszar krytyczny == (-infinity, -1.64)
ptest5 =  stats.norm.cdf(z5)
print(ptest5)
#mamy za malo dowodow zeby twierdzic ze H0 jest nieprawidlowa nie odrzucamy jej p>alfa
##ZADANIE 6 test obustronny H0= wariancja =4
#HA = sigma kwadrat nie jest rowna 4
n6 = 12
df6 = n6 - 1
skwadrat = 1.92
chi26 = ((n6 - 1)*skwadrat) / 4
alfa6 = 0.05
wk16 = stats.chi2.ppf(1-alfa6/2,df6)
wk26 = stats.chi2.ppf(alfa6/2,df6)
print(chi26)
print(wk16)
print(wk26)

