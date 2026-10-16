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
if (rok%4==0 and (rok%100!=0 or rok%400==0)):
    print(f"Rok {rok} je prestupny")
else:
    print(f"Rok {rok} neni prestupny")

prestupne = []
neprestupne = []

for rok in range(1890, 2031,1):
    if rok%4==0 and (rok%100!=0 or rok%400==0):
        prestupne.append(rok)
    else:
        neprestupne.append(rok)

d1=len(prestupne)
for i in range(0, len(prestupne), 10):
    print(prestupne[i:i+10])


#Prvočísla
#1
cislo=int(input("Zadejte cele cislo:"))
b=0
for i in range(2,cislo,1):
    if cislo%i==0:
        b+=1
    
        
if b==0:
    print(f"{cislo} je prvocislo")
else:
    print(f"{cislo} neni prvocislo")
    
    #2
prvocisla = []

# Внешний цикл перебирает каждое число от 2 до 100
for n in range(2, 101):
    # Внутренний цикл ищет делители числа n (до корня из n)
    for i in range(2, n):
        if n % i == 0:
            break  # Нашли делитель — значит, число не простое, прерываем внутренний цикл
    else:
        # Этот блок else выполнится ТОЛЬКО если цикл выше завершился без break,
        # то есть делителей не нашлось вообще -> это простое число!
        prvocisla.append(n)

print("Prvočísla:", prvocisla)
print("Počet:", len(prvocisla))
'''
#3
cislo=int(input("Zadejte cislo:"))






