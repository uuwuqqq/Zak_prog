'''
#ukol a)
def vitani(): #definice funkce
    name=str(input("Zadejte sve jmeno:"))  
    prijmeni=str(input("Zadejte sve prijmeni:"))
    cele_jmeno=name+" "+prijmeni
    print("Welcome to the event,",cele_jmeno,"!")
vitani() #volani funkce


#ukol b)

def kontrola(vek):
    if vek>=18:
        print(f"Vstup povolen")

    else:
        print(f"Vstup neni povolen")
vek=int(input("Zadejte svuj vek"))
kontrola(vek)


#ukol c)
def pocitani_ceny(isic_cena,cela_cena): #
    if isic_cena:
        konecna_cena=cela_cena*0.7
    else:
        konecna_cena=cela_cena 
    return konecna_cena

cela_cena=1800
otazka=input("Mate ISIC? Ano/Ne:")
isic_cena=otazka.lower()=="ano"
cena=pocitani_ceny(isic_cena,cela_cena)
print(f"To bude stat: {cena} Kc")


#ukol d)
def valide_email(email):
   if "@" in email and "." in email:
      return True
   else:
      return False
email=input("Zadejte svuj email:")
is_valide=valide_email(email)
print(f"Email je validni: {is_valide}")


#ukol e)

ucastniky=["Martin Novak", "Jana Svobodova", "Petr Novak"]
def pridat_ucastniky():
    jmeno=input("Zadejte jmeno a prijmeni ucastnika:")
    prijmeni=input("Zadejte prijmeni ucastnika:")
    cele_jmeno=jmeno+" "+prijmeni
    ucastniky.append(cele_jmeno)
    print(f"Seznam ucastniku: {ucastniky}")
    otazka=input("Chcete pridat dalsiho ucastnika? Ano/Ne:")
    if otazka.lower()=="ano":
        pridat_ucastniky()
    else:
        print("Konec pridavani ucastniku.")
        print(f"Seznam ucastniku: {ucastniky}")
pridat_ucastniky()
   

#ukol f)
def pocet_ucastniku():
    return len(ucastniky)
print(f"Pocet ucastniku:{pocet_ucastniku()}")


# ukol g)
def kontrola_kapacity():
    kapacita=7
    if len(ucastniky)>=kapacita:
        print("Kapacita je naplnena.")
    else:
        print("Kapacita neni naplnena.")
kontrola_kapacity()


#ukol h)

def vytvoreni_id():
    jmeno=input("Zadejte sve jmeno:")
    datum_narozeni=input("Zadejte datum narozeni (DD.MM.RRRR):")
    id=jmeno.upper()+datum_narozeni.replace(".","")
    return id
print(f"Vase ID je: {vytvoreni_id()}")
'''

#ukol i)
ucastniky=["Martin Novak", "Jana Svobodova", "Petr Novak"]
participants = ucastniky
def print_participants(participants):
    for participant in participants:
        print(participant)
print_participants(participants) 
