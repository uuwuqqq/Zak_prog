#1 hmotnosti trubky
'''
import math

def circle_area(d):
    radius = d / 2
    return math.pi * radius * radius

def tube_cross_section(d_out, d_in):
    # Используем circle_area, как просили в условии
    return circle_area(d_out) - circle_area(d_in)

def tube_mass(d_out, d_in, length, density=7850):
    area = tube_cross_section(d_out, d_in)  # вызываем функцию сечения
    return area * length * density

# Проверка
print(f"Hmotnost ocelove trubky: {tube_mass(0.060, 0.050, 6):.2f} kg")
print(f"Hmotnost hlinkove trubky:{tube_mass(0.060, 0.050, 6, 2700):.2f} kg")
'''
#2 prevod teplot
def convert_temperature(value, from_unit, to_unit):
    if from_unit=="C":
        if to_unit=="F":
            return value*1.8+32
        elif to_unit=="K":
            return value+273.5

    if from_unit=="F":
            if to_unit=="C":
                return (value-32)/1.8
            elif to_unit=="K":
                return (value-32)/1.8+273.5
    if from_unit=="K":
                if to_unit=="C":
                    return value-273.5
                elif to_unit=="F":
                    return (value-273.5)/1.8+32
    if from_unit==to_unit:
         return value
    else:
         print("Neplatna jednotka teploty")
         return None
'''   
from_unit=input("Zadejte jednotku teploty ze ktere prevadite(C,F,K):").upper()
to_unit=input("Zadejte jednotku teploty do ktere prevadite(C,F,K):").upper()
value=float(input("Zadejte hodnotu teploty:"))  
result=convert_temperature(value, from_unit, to_unit)
if result!=None:
     print(f"Prevedena hodnota:{result}")
'''     
c_f=[]     
for i in range(-40, 101):
     from_unit="C"
     to_unit="F"
     value=i
     f=convert_temperature(value, from_unit, to_unit)
     c_f.append(f"{f:.2f}")


c_k=[]
for b in range(-40, 101):
     from_unit="C"
     to_unit="K"
     value=b
     f=convert_temperature(value, from_unit, to_unit)
     c_k.append(f"{f:.2f}")


c=[]
for g in range(-40,101):
     c.append(g)

print("C to F and to K conversion table:")
for a, b, c in zip(c, c_f, c_k):
     print(f"{a} C = {b} F = {c} K")




                
            

           


    
    