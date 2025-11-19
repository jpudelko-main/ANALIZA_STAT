import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#zadanie nr 2 z zestawu 4
lista2 = [13, 13, 17, 7, 22, 22,
26, 17, 13, 14]
#lista2 = [16, 10, 16, 7, 17, 8, 6, 11, 21]
print(np.quantile(lista2, 0.25))
print(np.quantile(lista2, 0.5))
print(np.quantile(lista2, 0.75))
#rozstep = R = max-min
#rozstep kwartylowy = Q3-Q1
# odchylenie cwiartkowe = Q =QR/2
#wspolczynnik zmiennosci M Q/M
#zadanie nr 3 z zstawu 4
listaz3 = [3, 6, 2, 1, 1, 5]
sigma = np.std(listaz3, ddof=1)
print(sigma)
qwantyldol = np.quantile(listaz3, 0.25)
qwantylsrodek = np.quantile(listaz3, 0.5)
qwantylgora = np.quantile(listaz3, 0.75)
rozstepkwantytyl = qwantylgora - qwantyldol
maxymalna = max(listaz3)
minimalna = min(listaz3)
rozstep = maxymalna - minimalna
print(rozstep)
print(rozstepkwantytyl)
odchyleniecwiart = rozstepkwantytyl/2
wspolczynnikzmiennM = odchyleniecwiart/qwantylsrodek
print(odchyleniecwiart)
print(wspolczynnikzmiennM)
print(qwantyldol)
print(qwantylgora)
#zadanie 4
dane = [13, 13, 17, 7, 22, 22, 26, 17, 13, 14]
#[M-3*odchylenie cwiartkowe, M+3*odchylenie cwiartkowe] lub[M-1.5*odchylenie cwiartkowe, M+1.5*odchylenie cwiartkowe]
#Q3 = np.quantile(dane,0.75)
#Q1 = np.quantile(dane, 0.25)
#Q2 = np.quantile(dane,0.5)
#rozstepQ = Q3-Q1
#odchyleniecwiartk = rozstepQ/2
#daneodstajace1 = [Q2-1.5*odchyleniecwiartk, Q2+1.5*odchyleniecwiart]
#daneodstajace2 = [Q2-3*odchyleniecwiartk, Q2+3*odchyleniecwiart]
#print(daneodstajace1)
#print(daneodstajace2)
#zadanie 5
x = [37, 39, 39, 41, 45, 46, 48, 48, 52, 59, 59, 61, 61, 61, 64, 67, 69, 69, 73]
Q1 = np.quantile(x, 0.25)
Q2 = np.quantile(x, 0.5)
Q3 = np.quantile(x, 0.75)
#plt.hist(x,bins = 4,density = 1,cumulative=(1))
#plt.show()
binsss = np.sqrt(19) 
print(binsss)
#pierwiastek z ilosci n = 4.35889 zaokragalm do 4 density w plt = normalizcja zeby mial wykres pole 1 bins = ilosc klas
# kumulatywny sumuje wszystko na lewo wychodzi nam w dystrybuante 
#zadanie 6 w domu
xy = [23, 8, 15, 35, 21, 20, 10, 4, 28, 12, 9, 7, 24, 25, 31, 26, 23, 17, 13, 33, 29, 27, 24, 22, 32, 16, 9, 29, 22, 20, 8, 16, 21, 25, 31, 29, 23, 15, 32, 22, 23, 19, 24, 15, 21, 20, 29, 27, 23, 19, 16, 18, 24, 31, 28, 21, 8, 17, 24, 13, 12, 18, 23, 25]
danedom = pd.DataFrame(xy)
state = danedom.describe()
print(f"dane z 6 w domu:{state}")
plt.hist(danedom,8,density=(1),cumulative=(1))
sredniadomowe = state.mean()
plt.legend()
plt.show()
#zadanie 7
waga = pd.read_excel("C:\\Users\\jpude\\OneDrive\\Pulpit\\Waga.xlsx","Arkusz1",index_col=None,na_values = ["NA"])
#pandas --- Waga['Waga'](odwolanie do kolumny)std,mean(),quantile([lista])
waga.mean()#
#waga.hist(bins= 6,density = 1,cumulative = (1))
srednia = waga['Waga'].mean()

#waga['Waga'].hist(bins = list(range(50,85,5)),rwidth=0.85,density = 1,cumulative =1)
wzrost = pd.read_excel("C:\\Users\\jpude\\OneDrive\\Pulpit\\rzeczy do python anal.stat\\Wzrost.xlsx","Arkusz1")
sredniawzrost = wzrost["Wzrost"].mean()
wzrost['Wzrost'].hist(bins = list(range(145,195,5)),density = 1)
plt.show()