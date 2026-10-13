'''
diameters = [25.01, 24.97, 25.06, 25.00, 24.94, 25.03, 25.05, 24.95, 25.10, 24.99]
i=0
b=0
for position, diametr in enumerate (diameters, start=1): # enumerate with position starting from 1
    if 24.95<=diametr<=25.05:
        print(position,".",diametr, "mm: Ok") 
        b=b+1
    elif diametr<24.95:
         print(position,".",diametr, "mm: Maly")
         i=i+1
         b=b+1
    else:
        print(position,".",diametr, "mm: Velky") 
        b=b+1
        i=i+1
c=i/b*100
print("Zmetku:", i, "z", b, "(",c,"%)")       
#roky
rok=int(input("Zadejte rok:"))
print(rok, "je prestupny") if (rok %4 == 0 or rok%400 == 0) else print ("rok",rok, "neni prestupny")
''' 
prestupne=[]
nepr=[]
for rok1 in range(1800,2031,1):
    if rok1%4==0 or rok1%400==0:
        prestupne.append(str(rok1))
    else:
        nepr.append(str(rok1))

for i in range(0, len(prestupne), 10):
    # Берем срез из 10 элементов и соединяем их пробелом или запятой
    radek = " ".join(prestupne[i:i+10])
    print("Prestupne roky:",radek)


