#ukol1
'''
with open("zprava.txt", "a", encoding="utf-8") as file:
    file.write("Hello world!\n")
    file.write("loh!\n")
    file.write("GG!\n")

with open("zprava.txt", "r", encoding="utf-8") as file:
    content=file.read()
print(content)


with open("zprava.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line) 

with open("zprava.txt", "r", encoding="utf-8") as file:
    for line in file:
        line=line.rstrip()
        if line:
            print(line)
    
try:
    with open ("denik.txt", "r", encoding="utf-8") as file:
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("Tento file neexistuje.")


from datetime import datetime
message=input("Zadejte zpravu")
with open ("denik.txt", "a", encoding="utf-8") as file:
    time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file.write(f"{time}-{message}\n")
print("Zprava byla ulozena.")
'''
from pathlib import Path
path=Path("denik.txt")
path.parent.mkdir( exist_ok=True)
path.write_text("Ready\n", encoding="utf-8")
path.read_text(encoding="utf-8")    
print(path.read_text(encoding="utf-8"))