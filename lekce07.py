#1
'''
def text_statistics(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            a = 0
            b = 0
            c = 0
            radky = []
            
            for line in file:
                line = line.rstrip("\n")
                if line:
                    print(line)
                    a += 1
                    words = line.split()
                    b += len(words)
                    c += len(line)
                    radky.append(line)
            
            # Находим самую длинную строку один раз после чтения всего файла
            radek_max = max(radky, key=len) if radky else ""
            return a, b, c, radek_max

    except FileNotFoundError:
        print("Soubor nebyl nalezen.")
        return 0, 0, 0, ""
print("Pocet neprazdnych radku, slov a znaku a nejdelsi radek:", text_statistics("soubor.txt"))

#2
from datetime import datetime   
def add(poznamka):
        with open("journal.txt", "a", encoding="utf-8") as file:
            time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"{time}, | {poznamka}\n")
            return True
def my_list():
    try:
        with open("journal.txt", "r", encoding="utf-8") as file:
             for line in file:
                  line=line.rstrip("\n")
                  if line:
                       print(line)
                    
    except FileNotFoundError:
         print(f"File doesnt exist")
         return False
def search(keyword):
     try:
            with open('journal.txt', 'r', encoding='utf-8') as file:
                  for line in file:
                        if keyword.lower() in line.lower():  # .lower() делает поиск нечувствительным к регистру
                            print(f" Todle je tato poznamka{line.strip()}")
                            return True
                  
                                          
     except FileNotFoundError:
        print(f"File doesnt exist")
        return False
     
        
vyber = input(
    "Mate na vyber 3 funkce:\n"
    "Pridat novou poznamku: napiste Pridat\n"
    "Precist vsechy poznamky: napiste Cist\n"
    "Najit poznamky podle klicoveho slova: napiste Najit\n> "
)

if vyber.upper() == "PRIDAT":
    poznamka = input("Zadejte poznamku: ")
    # add(poznamka)
elif vyber.upper() == "CIST":
    my_list()
elif vyber.upper() == "NAJIT":
    search(keyword=input("Zadejte klicove slovo: "))

#3
def load_measurmeters(path):
    time_list = []
    temp_list = []
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:  # пропускаем пустые строки
                    continue
                
                time, temp = line.split(";")
                
                try:
                    temp_float = float(temp)        # пробуем перевести в число
                    temp_list.append(temp_float)     # если удалось — сохраняем число
                    time_list.append(time)          # и время
                except ValueError:
                    pass  # если там 'chyba', просто пропускаем эту строку

        return time_list, temp_list

    except FileNotFoundError:
        print("File doesnt exist")
        return False

times, temps= load_measurmeters("measurements.txt")
a=zip(times, temps)
print(list(a))

def summarize(temps):
    try:
        temp_float = float(temp)        # пытаемся перевести в float
        temp_list.append(temp_float)     # если получилось — сохраняем число
        time_list.append(time)          # и сохраняем время
    except ValueError:
        pass

    i=0
    b=0
    
def summarize(temps):
    minimum = min(temps)
    maximum = max(temps)
    prumer = sum(temps) / len(temps)  # сумма всех элементов / количество
    
    return maximum, minimum, prumer

print("Nejvetsi temp, nejmensi, prumer tempt:",summarize(temps))

def write_report(path):
    with open(path, "a", encoding="utf-8" ) as file:
        file.write(temps)
        file.write(maximum,minimum, prumer)


#4
from pathlib import Path 
def prejmenovani(slozka):
    fotky=[]
    for path in Path(slozka).iterdir():
        if path.is_file() and path.suffix.lower() in {".jpg", ".jpeg"}:
            fotky.append(path)
    return fotky
file_pathes=prejmenovani("Photos")
n=0
for foto in file_pathes:
    n+=1
    new_file_path=foto.with_name(f"photo_{n:03}" + f"{foto.suffix.lower()}")
    if new_file_path.exists():
        
        print(f"foto s jmenem {new_file_path} uz existuje")
            
    else:
        print(new_file_path)

otazka=str(input("Vyhovujou vam ta nova jmena? Ano/Ne?"))
i=0
if otazka.lower()=="ano":
    for foto in file_pathes:
        
        i+=1
        new_file_path=foto.with_name(f"photo_{i:03}" + f"{foto.suffix.lower()}")
        if new_file_path.exists():
            pass
            
        else:
            foto.rename(new_file_path)
'''
#5

with open("Cisla_.txt", "a", encoding="utf-8") as file:
    for i in range(1,65536):
        file.write(f"{i}\n")
with open("Cisla_bytes.txt", "ab",) as file:
    for i in range(1,65536):
        byte_data=i.to_bytes(length=2, byteorder='big', signed=False)
        file.write(byte_data)

                  
                  









    























   






                       
                   
    
      


