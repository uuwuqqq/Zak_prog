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

#3

cislo = int(input("Zadejte cislo: "))
prvocinitele = []

# Перебираем простые числа, которые мы уже нашли ранее
for p in prvocisla:
    while cislo % p == 0:
        prvocinitele.append(p)
        cislo = cislo // p
    if cislo == 1:
        break

print("Prvočinitele:", prvocinitele)

vyska=int(input("Zadejte liche cislo:"))
while vyska%2==0 or vyska<1:
    print(vyska,"neni liche cislo")
    vyska=int(input("Zadejte LICHE cislo:"))

for i in range(1, vyska+1,2):
    mezery=(vyska-i)//2
    print(" "*mezery+"*"*i)
for i in range(vyska-2,0,-2):
    mezery=(vyska-i)//2
    print(" "*mezery+"*"*i)
     
for p in range(100, 1000):
       i=str(p)
       a=int(str(i)[0])
       b=int(str(i)[1])
       c=int(str(i)[2])
       if a**3 + b**3 + c**3 ==p:
              print(p)
 

a = 2
b = 3
t = 0
tolerance = 1e-6  # требуемая точность 10^(-6)

# Цикл работает, пока размер отрезка больше точности
while (b - a) > tolerance:
    c = (a + b) / 2  # ОБЯЗАТЕЛЬНО пересчитываем середину внутри цикла!
    t += 1           # Считаем итерации
    
    # Значения функции в точках
    f_c = c**3 - 2*c - 5
    f_a = a**3 - 2*a - 5
    
    # Проверяем знак, чтобы понять, куда сдвигать границы
    if f_a * f_c < 0:
        b = c
    else:
        a = c

print("Počet iterací:", t)
print("Kořen:", c)




#Sikmy vrh
import math
V=int(input("Zadejte pocatkovou rychlost:"))
a=int(input("Zadejte uhel vrhu ve stupnich:"))
a = math.radians(a)  # převod úhlu na radiány
V_x=V*math.cos(a)
V_y=V*math.sin(a)
t=0.0001
dolet=[]
vyska=[]
cas=[]
while t*V_y - 0.5*9.81*t**2 >=0 :
    y=t*V_y - 0.5*9.81*t**2
    x=t*V_x
    print(f"t={t:.5f}, x={x:.5f}, y={y:.5f}")
    dolet.append(x)
    vyska.append(y)
    cas.append(t)
    t=t+0.0001
print("dolet:",f"{max(dolet):.2f}")
print("vyska:",f"{max(vyska):.2f}")
print("cas:",f"{max(cas):.2f}")

 ''' 







  








    








