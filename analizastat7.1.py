#Zadanie 1 zestaw zadan nr 8
# H0 : p1 =1/6, p2=1/6,p3=1/6...p6=1/6
#HA = p1=/=1/6,.....p6=/=1/6
#poziom istotnosci = alfa=0.01
#liczba stopni swobody = ddof = 5
import scipy.stats as stats
import numpy as np
alfa1 = 0.01
obs1 = [14, 15, 27, 13, 22, 29]
exp = [20, 20, 20, 20, 20, 20]
chi1 = stats.chisquare(obs1,exp)
print(chi1)
#wartosc funkcji testowej = 12.2
#p = 0.032
#p>alfa1 --> nie odrzucamy hipotezy zerowej na poziomie istotnosci  alfa 0.01
#zadanie nr 2 zestaw 8
#H0 : p1 = 9/16 p2 = 3/16 p3 = 3/16 p4=1/16
#Ha : p1=/=9/16...., p4=/=1/16
#poziom istotnosci  = alfa= 0.05
alfa2 = 0.05
#ddof = 3 (4-1)
obs2 = np.array([315,108,101,32])
exp = 556*np.array([9/16,3/16,3/16,1/16])
print(exp)
chi2 = stats.chisquare(obs2,exp)
print(chi2)
#wartosc funkcji testowej  = 0.47
#p value = 0.92(prawdopod.statystyczne)
#p>alfa --> nie ma powodu do odrzucenia funkcji na poziomie istotnosci 0.05
# Wyniki sa zgodne z zakladanym rozkladem 


#Zadanie nr 3 zestaw 8
# X-wystepowanie choroby wiencowej 
# Y - Wystepowanie nadcisnienia 
#H0 zmienne X i Y sa niezalezne Wystepowanie Podwyzszonego cisnienia nie jest zalezne od wystepowania
#choroby wiencowej 
# k = 2(ilosc wynikow w zmiennej X)
# s =  2 (ilosc wynikow w zmiennej Y )
# r  = ddof r = (k-1)*(s-1)
obs3 = np.array([[37,17],[8,38]])
chi3 = stats.chi2_contingency(obs3,correction = 0)#correction 0 lub 1 (poprawka yates jak nie spelnione zalozenia)
print(chi3)
#chi2 = 24.02(dla correction = 1),pvalue = 8.63 do minus 7(dla z correction 1)# df = 1 ,ten array co drukuje to oczekiwane wart.
# p<alfa - odrzucamy H0 - zmienne X i Y sa zalezne -->wystepowanie choroby wiencowa jest zwiazana z wystepowaniem nadcisnienia
# corrrection = poprawka yates'a my spelniamy zalozenia wiec nie musimy wiec correction = 0
# zadanie nr 4 zestaw 8
#H0 = Populacje z ktorych pochodza proby sa jednorodne 
#HA = Populacje z ktorych pochodza proby nie sa jednorodne
#proby to lata zestawiony w tabelce jest procent zgonow u noworodkow 
#jednorodny procent smierci noworodkow
obs4 = np.array([[1594,61],[1906,41],[1818,42],[2423,50],[2372,51]])
print(obs4)
chi4 = stats.chi2_contingency(obs4,correction=0)
print(chi4)
#chi2 = 15.13, ddoff = 4,p = 0.0044 alfa = 0.05
#p<alfa - sa podstawy do odrucenia H0 
#zadanie 5 zestaw zadan nr 8
alfa5 = 0.05
#X = typ terapi
#Y-Wyzdrowienie /Niewyzdrowienie
#H0 = X i Y zmiennne niezalezne Nie widzimy roznicy w wyzdowieniach w zaleznosci od terapii
#HA = X i Y sa zalezne . Widzimy w wyzdrowieniach roznice w zaleznosci od terapii
#test niezaleznosci chi 2
obs5 =  np.array([[8,2],[2,8]])
print(obs5)
#N BARDZO MALE STOSUJEMY DOKLADNY TEST FISHERA MA TAKA SAMA H0 I HA
fiszer = stats.fisher_exact(obs5)
print(fiszer)
#16 = iloraz szans pvalue 0.023
#p<alfa5 ---> odrzucamy H0 
#odp. zmienne sa zalezne lepiej dziala antybiotyoterapia niz sok zurwinowy 