'''
#Převodník délek
delka=float(input("Zadej delku mm:"))
print("Delka [mm]:", delka)
cm=delka/10
m=cm/100
inch=delka/25.4
print(f"{delka:.3f} mm =" f"{cm:.3f} cm =" f"{m:.3f}m=" f"{inch:.3f}in" )

#Sekundy na hodiny
cas=int(input("Zadej cas v sekundach:"))
h=cas//3600
m=cas%3600//60
s=cas%3600%60
print(f"{h}:" f"{m:02}:" f"{s:02}") # :02 znamená, že číslo bude vytištěno s minimálně dvěma číslicemi, doplněno nulami zleva pokud je potřeba

#Rozbor slova
slovo=str(input("Zadej slovo:"))
pocet_znaku=len(slovo) #len vrací počet znaků ve stringu
prvni_znak= (slovo[0]) #první znak ve stringu len(x[0])
posledni_znak=(slovo[-1]) #posledni znak  len(x[-1])
vel=slovo.upper() #převede celé slovo na velká písmena
zpatky=slovo[::-1] #převede celé slovo obráceně

print("Slovo:", slovo)
print("Pocet znaku:", pocet_znaku)
print("Prvni znak:", prvni_znak)
print("Posledni znak:", posledni_znak)
print("Velkymi pismeny:", vel)
print("Pozpatky:", zpatky)
if slovo == zpatky:
    print("Paindrom: True")
else:
    print("Paindrom: False")
   
#Rozsahy celých čísel
bit=int(input("Zadejte pocet bitu:"))
roz_max=2**(bit)-1
roz_min1=roz_max//(-2)
roz_max1=roz_max//2
print(f"{bit} bitu: 0 az {roz_max},"  f"{roz_min1} az {roz_max1}")
 '''
#Dvojková soustava ručně
cislo=int(input("Zadej nezaporne cele cislo"))
