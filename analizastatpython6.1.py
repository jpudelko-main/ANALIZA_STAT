#  zadanie 1 zestaw 7
import scipy.stats as stats
import pandas as pd
import matplotlib.pyplot as plt
srednia1 =59.01
s1 = 44.89
n1 = 53
srednia2 = 46.61
s2 = 34.85
n2 = 54
#funkcja testowa
from math import sqrt
z = (srednia1 - srednia2)/sqrt(s1**2/n1+s2**2/n2)
print(z)
alfa = 0.01
wk = stats.norm.ppf(1-alfa/2)
print(wk)
#obszar krytyczny od -nieskinczonosc do -2.58 suma <2.58 , +nieskonczonosc)
#wniosek nie ma podstaw do odrzucenia Hipotezy zerowej 
p = 2 *(1- stats.norm.cdf(z))
print(p)
#nie ma podstaw do odrzucenia h0 czemu p tak wyglada bo chcey policzyc na prawo od z
#dlatego 1-stats norm cdf bo cdf liczy nam dystrybuante na lewo  odejmiem od 1 i jest klasa bo mamy na prawo
inna = stats.ttest_ind_from_stats(mean1 =59.01, std1= 44.89, nobs1 = 53, mean2 = 46.61, std2 = 34.85, nobs2 = 54, equal_var = 0)
print(inna) #ta funkcja weaca nam wartosc funkcji testowej i wartosc p (prawdopodobienstwo statystyczne) 
#wiecej info na temat funkcji testowej i zalozen masz w zeszycie 
#zadanie 2 zestaw 7 
#osoby ktore moga przyjac dana kuracje odchudzajaca
#h0  : mi1 = m2 taki sam ubytek wagi w w populacji 1 i populacji 2 
#Ha  : mi1 =/=m2 inny ubytek wagi w populacji 1 i populacji 2
#Zalozenia ; proby pochodza z populacji o rozkladach normalnych,wariancje sa rowne  
#nie siegamy po ten sam test co w zadaniu 1 bo n<30 (male populacje)

n12 = 16
x12 = 5.4
s12 = 2.4
n22 = 11
x22 = 3.4
s22 = 2.8
alfa2 = 0.05
t = (x12 -x22)/sqrt(((n12-1)*s12**2+(n22-1)*s22**2)/(n12+n22-2)*(1/n12 + 1/n22))
print(t)
df =n12 +n22 -2
#wartosc krytyczna 
wk2 = stats.t.ppf(1-alfa2/2,df)
print(wk2)
#obszar krytyczny (-infinity, -2.06> U <2.06,+infinity)
p2 = 2*(1- stats.t.cdf(abs(t),df))
print(p2)
#0.057> alfa2
#0.057 jest wieksze od alfa 2 zatem odrzucamy hipoteze zerowa

inna2 = stats.ttest_ind_from_stats(mean1 = 5.4,std1 =2.4,nobs1 = 16,mean2 = 3.4,std2 = 2.8,nobs2 = 11 ,equal_var = 1)
print(inna2)
#zadanie 3 zestaw 7
#zalozenia w obu populacjach zmienne maja rozklad normalny bo jedna jest mala populacja a druga na granicy praktycznie 
#test dla roznych wariancji 
s1 = 5.29
s2 = 2.69
n1 = 15
n2 = 30
F = s1**2/s2**2
print(F)
#wartosci krytyczne
F1 = stats.f.ppf(alfa/2,n1-1,n2-1)
F2 = stats.f.ppf(1-alfa/2,n1-1,n2-1)
print('obszar krytyczny = ', F1,F2)
#prawdopodobienstwo statystyczne dla funkcji testowej f zroznicowania wariancji
p = 2*min(stats.f.cdf(F,n1-1,n2-1),1-stats.f.cdf(F,n1-1,n2-1))
print('prawd. stat.3 = ',p)
#zadanie 4
#h0 = mi1 = mi2 mi=0
#hA = mi1=/=mi2 HA; mi=/=0
dane = pd.read_excel(r"C:\Users\jpude\OneDrive\Pulpit\rzeczy do python anal.stat\Refluks.xlsx")
print(dane)
srednia_przed = dane['Przed'].mean()
srednia_po =dane['Po'].mean()
srednia_roznic= dane['Różnica'].mean()
print(srednia_przed,srednia_po,srednia_roznic)
n = dane['Różnica'].count()
print(n)


dane.hist('Różnica')
plt.show()
dane.hist('Przed')
plt.show()
dane.hist('Po')
plt.show()
#test Shapiro Wilka H0; dane pochodza z populacji o rozkladie normalnym
#Ha dane nie pochodza z populacji o rozkladzie normlanym
shapiro1 = stats.shapiro(dane['Różnica'])
shapiro2 = stats.shapiro(dane['Przed'])
shapiro3 = stats.shapiro(dane['Po'])
print(shapiro1,shapiro2,shapiro3)
testz4 = stats.ttest_1samp(dane['Różnica'],popmean = 0)
print(testz4)
#pvalue z ttest jest wieksze od alfy 0.08> 0.05 nie mamy powodow zeby twierdzic ze h0 jest zle
testz42 = stats.ttest_rel(dane['Przed'],dane['Po'])
print(testz42)
###5/7
s1 = 5.1
s2 = 3.0
n1 = 13
n2 = 15
F = s1**2/s2**2
print(F)
#wartosci krytyczne
F1 = stats.f.ppf(alfa/2,n1-1,n2-1)
F2 = stats.f.ppf(1-alfa/2,n1-1,n2-1)
print('obszar krytyczny = ', F1,F2)
#prawdopodobienstwo statystyczne dla funkcji testowej f zroznicowania wariancji
p = 2*min(stats.f.cdf(F,n1-1,n2-1),1-stats.f.cdf(F,n1-1,n2-1))
print('prawd. stat.5 = ',p)

import scipy.stats as stats
from math import sqrt
import statistics as st
import matplotlib.pyplot as plt
import pandas as pd

#Zestaw7
#zadanie1
alpha = 0.01
sred1 = 59.01
sred2 = 46.61
n1= 53
n2  = 54
s1 = 44.89
s2= 34.85
z = (sred1 - sred2)/sqrt(((s1**2)/n1)+((s2**2)/n2))
print(z)#funkcja testowa
wk = stats.norm.ppf(1-alpha/2)
print(wk)
p = 2*(1-stats.norm.cdf(z))
print(p)
stats.ttest_ind_from_stats(mean1=59.01,std1=44.89, nobs1=53,mean2=46.61,std2=34.85,nobs2=54,equal_var=0)

#zadanie2
alpha = 0.01
sred1 = 5.4
sred2 = 3.4
n1 = 16
n2 = 11
s1=2.4
s2 = 2.8
t = (sred1 - sred2)/sqrt(((((n1-1)*(s1**2))+(n2-1)*(s2**2))/(n1 +n2-2))*((1/n1)+(1/n2)))
print(t)
wk = stats.norm.ppf(1-alpha/2)
print(wk)

#zadanie3
#zadanie 7
sred1 = 19.16
sred2 = 9.53
s1 = 5.29
s2 = 2.69
n1 = 15
n2 = 30
alfa = 0.05
t = (sred1 - sred2)/sqrt(((((n1-1)*(s1**2))+(n2-1)*(s2**2))/(n1 +n2-2))*((1/n1)+(1/n2)))
print(t)

#zadanie 8
n1= 102
n2 = 102
r1 = 29
r2 = 34
phat1 = r1/n1
phat2 = r2/n2
print(phat1, phat2)
#FUNKCJA TESTOWA
pline = (r1 + r2)/(n1 + n2)
sigma = sqrt(pline*(1-pline)*(1/n1+1/n2))
z = (phat1 - phat2)/sigma
print(z, pline)

A =[5, 6, 12, 9, 8, 5, 7, 8, 15, 7]
B = [6, 5, 11, 5, 3, 4, 6, 6, 4, 9, 3, 2]
sredA = st.mean(A)
sA = st.stdev(A)
nA = len(A)
sredB = st.mean(B)
sB = st.stdev(B)
nB = len(B)
print(sredA, sA, nA)
print(sredB, sB, nB)
#hipoteza zerowa średni spadek ciśnienia po podaniu leku jest taki sam
#stosujemy test t dla zmiennych niepowiązanych
#krok1 sprawdzamy czy próby  pochodzą z populacji o rozkładach normalnych
res1 = stats.shapiro(A)
print(res1)
res2 = stats.shapiro(B)
print(res2)
#p większe od alfa więc  próba pochodzi z populacji o rozkłądzie normalnym
#Wniosek: próby  pochodzą z populacji o rozkładach normalnych
#dzięki temu że próby pochodzą z pop o rozkł norm, możemy zostać przy teście parametrycznym


####
from math import sqrt 
from scipy import stats
import pandas as pd
import numpy as np
import statistics as st

###3/7
#test dla zmiennych niezaleznych
srednia1 = 19.16
srednia2 = 9.53
s1 = 5.29
s2 = 2.69
n1 = 15
n2 = 30
alfa = 0.05
#funkcja testowa
t = (srednia1-srednia2)/sqrt(s1**2/n1+s2**2/n2)
print('t = ',t)
w1 = s1**2/n1
w2 = s2**2/n2
df = (w1+w2)**2/(w1**2/(n1-1)+w2**2/(n2-1))
print('df = ',df)
#wartosc krytyczna
wk = stats.t.ppf(1-alfa/2,df)
print(wk)
#prawdopodobienstwo statystyczne
p = 2*(1-stats.t.cdf(abs(t),df))
print(p)
print(stats.ttest_ind_from_stats(mean1 = 19.16,std1 = 5.29,nobs1 = 15, mean2 = 9.53, std2 = 2.69, nobs2 = 30,equal_var = 0))


###5/7
s1 = 5.1
s2 = 3.0
n1 = 13
n2 = 15
F = s1**2/s2**2
print(F)
#wartosci krytyczne
F1 = stats.f.ppf(alfa/2,n1-1,n2-1)
F2 = stats.f.ppf(1-alfa/2,n1-1,n2-1)
print('obszar krytyczny = ', F1,F2)
#prawdopodobienstwo statystyczne dla funkcji testowej f zroznicowania wariancji
p = 2*min(stats.f.cdf(F,n1-1,n2-1),1-stats.f.cdf(F,n1-1,n2-1))
print('prawd. stat.5 = ',p)


####testy wariancjij dla poprzdnich zadan
##2/7
n1 = 16
n2 = 11
s1 = 2.4
s2 = 2.8
F = s1**2/s2**2
print(F)
#wartosci krytyczne
F1 = stats.f.ppf(alfa/2,n1-1,n2-1)
F2 = stats.f.ppf(1-alfa/2,n1-1,n2-1)
print('obszar krytyczny = ', F1,F2)
#prawdopodobienstwo statystyczne dla funkcji testowej f zroznicowania wariancji
p = 2*min(stats.f.cdf(F,n1-1,n2-1),1-stats.f.cdf(F,n1-1,n2-1))
print('prawd. stat.2 = ',p)

##3/7
s1 = 5.29
s2 = 2.69
n1 = 15
n2 = 30
F = s1**2/s2**2
print(F)
#wartosci krytyczne
F1 = stats.f.ppf(alfa/2,n1-1,n2-1)
F2 = stats.f.ppf(1-alfa/2,n1-1,n2-1)
print('obszar krytyczny = ', F1,F2)
#prawdopodobienstwo statystyczne dla funkcji testowej f zroznicowania wariancji
p = 2*min(stats.f.cdf(F,n1-1,n2-1),1-stats.f.cdf(F,n1-1,n2-1))
print('prawd. stat.3 = ',p)

##8/7
n1 = 102
r1 = 29
n2 = 102
r2 = 34
phat1 = r1/n1
phat2 = r2/n2
print('frakcja1 = ',phat1, '  frakcja2 = ',phat2)
#funkcja testowa
pline = (r1+r2)/(n1+n2)
sigma = sqrt(pline*(1-pline)*(1/n1+1/n2))
z = (phat1-phat2)/sigma
print('pline ',pline, '  sigma ',sigma)
print('funkcja testowa ',z)
#wartosc krytyczna
wk = stats.norm.ppf(1-alfa/2)
print('wartosc krytyczna: ',wk)
#prawdopodobienstwo statystyczne
p = 2*(1-stats.norm.cdf(abs(z)))
print(p)

##11/7
A = [5, 6, 12, 9, 8, 5, 7, 8, 15, 7]
B = [6, 5, 11, 5, 3, 4, 6, 6, 4, 9, 3, 2]
n1 = len(A)
n2 = len(B)
sredniaA = st.mean(A)
sredniaB = st.mean(B)
sA = st.stdev(A)
sB = st.stdev(B)
print('ileA ',n1,'ileB ',n2,'sredniaA ',sredniaA,'sredniaB ',sredniaB,'odchylenieA ',sA,'odchylenieB ',sB)

#test Shapiro-Wilka
print(stats.shapiro(A)) #test odnosi sie do calej listy danych
print(stats.shapiro(B))

#wariancje
F = sA**2/sB**2
print('F ',F)
#wartosci krytyczne
F1 = stats.f.ppf(alfa/2,n1-1,n2-1)
F2 = stats.f.ppf(1-alfa/2,n1-1,n2-1)
print('obszar krytyczny = ', F1,F2)
p = 2*min(stats.f.cdf(F,n1-1,n2-1),1-stats.f.cdf(F,n1-1,n2-1))
print('prawd. stat.11 = ',p)