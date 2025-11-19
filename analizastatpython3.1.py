import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#zad 9 zestaw 4
dane = pd.read_excel(r"C:\Users\jpude\OneDrive\Pulpit\rzeczy do python anal.stat\Antybiotyki2 (1).xls",sheet_name ='Dane 2')
print(dane)
DaneIlosciowe = pd.DataFrame(dane,columns=['Dni hospitalizacji','Wiek', 'WBC'])
print(DaneIlosciowe)
sredniawiek = dane['Wiek'].mean()
stdwiek = dane['Wiek'].std()
ogolne = dane['Wiek'].describe()
rozstep =DaneIlosciowe.max() - DaneIlosciowe.min()
print(DaneIlosciowe.describe())
#print(sredniawiek)
#print(ogolne)
print(rozstep)
print(dane.groupby(['Płeć']).mean())
print(dane.groupby(['Antybiotyk']).describe())
print(dane.groupby(['Płeć']).describe())
#Dane w pliku Antybiotyki2.xlsx s¡ cz¦±ci¡ wi¦kszej próby zebranej przez pewien szpital
#w badaniach dotycz¡cych antybiotyków. Wyznacz:
#(a) histogram dla wieku pacjentów,
#(b) histogram dla WBC z podziaªem na pªe¢.
dane.hist('Wiek',by = 'Płeć',bins = [10,20,30,40,50,60,70,80],density = 0,cumulative= 0)#density =pole pod wykresem =1,cumulative = tworzy sie ala dystrybuanta
plt.show()
#zadanie 12 zestaw 4
aptt = pd.read_excel(r"C:\Users\jpude\OneDrive\Pulpit\rzeczy do python anal.stat\APTT2.xls",sheet_name= 'Arkusz1')
print(aptt)
import seaborn as sns
sns.boxplot(aptt['Grupy'],aptt['APTT'])
plt.show()
aptt2 = pd.read_excel(r"C:\Users\jpude\OneDrive\Pulpit\rzeczy do python anal.stat\APTT2.xls",sheet_name= 'Arkusz2')
print(aptt2)
aptt2.boxplot()
plt.show()
#zadanie 13 
rozklady = pd.read_excel(r"C:\Users\jpude\OneDrive\Pulpit\rzeczy do python anal.stat\Rozkłady.xlsx")
print(rozklady)
wzrost = rozklady['Proba 1']
srednia = wzrost.mean()
print(srednia)
mediana = wzrost.median()
print(mediana)
skosnosc = wzrost.skew()
print(skosnosc)
plt.hist(wzrost)
plt.axvline(srednia, color='red' , label ="Srednia")
plt.axvline(mediana, color = "yellow", label = "mediana")
stdwzrost = wzrost.std()
print(stdwzrost)
plt.legend()
plt.show()
wiek = rozklady['Proba 2']
sredniawiek = wiek.mean()
print(sredniawiek)
medianawiek = wiek.median()
print(medianawiek)
skosnoscwiek = wiek.skew()
print(skosnoscwiek)
plt.axvline(sredniawiek, color='red' , label ="Srednia")
plt.axvline(medianawiek, color = "yellow", label = "mediana")
plt.legend()
plt.hist(wiek)
plt.show()
dlugosc_zycie = rozklady['Proba 3']
sredniazycie = dlugosc_zycie.mean()
print(sredniazycie)
medianazycie = dlugosc_zycie.median()
print(medianazycie)
skosnosczycie = dlugosc_zycie.skew()
print(skosnosczycie)
plt.axvline(sredniazycie, color='red' , label ="Srednia")
plt.axvline(medianazycie, color = "yellow", label = "mediana")
plt.hist(dlugosc_zycie)
plt.legend()
plt.show()
kola = rozklady['Proba 4']
sredniakola = kola.mean()
print(sredniakola)
medianakola = kola.median()
print(medianakola)
skosnosckola = kola.skew()
print(skosnosckola)
plt.axvline(sredniakola, color='red' , label ="Srednia")
plt.axvline(medianakola, color = "yellow", label = "mediana")
plt.hist(kola)
plt.legend()
plt.show()
###zestaw 4 sie skonczyl