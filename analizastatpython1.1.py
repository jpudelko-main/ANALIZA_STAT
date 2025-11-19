#zadanie 8 ZESTAW 3 ANALIZA.STAT
# Niech X b¦dzie zmienn¡ losow¡ równ¡ liczbie godzin, które studenci sp¦dzaj¡ w tygodniu
#korzystaj¡c z internetu. Wyznacz kwartyl dolny, Q1, kwartyl górny, Q3, percentyl, P90,
#dla zmiennej X o rozkªadzie normalnym z µ = 13.5 godziny i σ = 2.5 godziny. Obliczenia
#wykonaj w Excelu oraz Pythonie.#
import scipy.stats as stats
import math 
x = stats.norm.cdf(0, 0, 1)
print(x)
#stats.norm.cdf(x, args, kwds) potrzebne sa nam 3 argumenty :x ,u(mi) ,sigma domyslna wartosc --
# U=0 , sigma = 1
y = stats.norm.ppf(0.5, 0, 1)
print(y)
#po daniu prawdopodobienstwo na lewo od tej wartosci oddaje nam x 
#P(Z>z0.25) = 0.25
#P(Z>z0.8) = 0.8
z = stats.norm.ppf(0.75,0,1)
print(z)
f = stats.norm.ppf(0.2,0,1)
print(f)
#Z11 zestaw 3
z11 = stats.norm.cdf(79,78,13)

rozwiazanie11 = 1-z11
print(rozwiazanie11)
#podpunkt b 
sigma11 = 13/math.sqrt(20)
wynikb = 1 - stats.norm.cdf(79,78,sigma11)
print(wynikb)
#zadanie 13 zestaw 3 
wynik13 = stats.norm.cdf(206,202,14/6)- stats.norm.cdf(198,202,14/6)
print(wynik13)
# zadanie 14
odp14 = stats.chi2.cdf(30,26) 
print(odp14)
# zadanie 15 
#Znajd¹ χ
#2
#0.05,15. Obliczenia wykonaj w Pythonie.
#Dla α ∈ (0, 1), de
#niujemy tα,n w taki sposób, »e
#P(Tn ≥ tα,n) = α,
#gdzie Tn jest zmienn¡ o rozkªadzie t-Studenta o n stopniach swobody.
funkcja15 = stats.chi2.ppf(0.95,15)
print(funkcja15)
#zadanie 16
zadanie16 = stats.t.cdf(1.4,12)
print(zadanie16)
#zadanie 17
zadanie17 = stats.t.ppf(0.975,9)#0.975 bo 1-alfa a alfa to 0.025
print(zadanie17)
zadanie18 = 1- stats.f.cdf(1.5,6,14)
print(zadanie18)
#zadanie 19
zadanie19 = 1-stats.binom.cdf(89,1000,0.1)# 89 dla mniejszych roqnych 89 to nie jest ciagla to jest dyskrretna gdybym dal 90 to bym dostal prawdopodob wieksze rowne 91
print(zadanie19)
zadanie19n = 1- stats.norm.cdf(90,100,math.sqrt(90))
print(zadanie19n)
import numpy as np
from scipy import stats
#zadanie 2 
lista2 = [13,13,17, 7, 22, 22,
26, 17, 13, 14]
#lista2 = [16, 10, 16, 7, 17, 8, 6, 11, 21]
print(np.quantile(lista2, 0.25))
print(np.quantile(lista2, 0.5))
print(np.quantile(lista2, 0.75))