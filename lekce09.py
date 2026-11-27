import json as j
#1
games = [
    {"title": "Portal", "year": 2007, "completed": True},
    {"title": "Hades", "year": 2020, "completed": False},
    {"title": "Celeste", "year": 2018, "completed": True},
]

with open("games.json", "w", encoding="utf-8") as file:
    j.dump(games, file, ensure_ascii=False, indent=2)

with open("games.json", "r", encoding="utf-8") as file:
    games_loaded=j.load(file)
print("Games, that are finished:")    
for game in games_loaded:
    if game["completed"]==True:
        print(game["title"], game["year"])
#2
with open("games.json", "r", encoding="utf-8") as file:
    games_loaded2=j.load(file)
for game in games_loaded2:
    if game["title"]=="Hades":
        game["completed"]=True
with open("games_updated.json", "w", encoding="utf-8") as file:
    j.dump(games_loaded2, file, ensure_ascii=False, indent=2 )
print("Status was changed:")  
for game in games_loaded2:
        print(game["title"], game["year"], game["completed"])

#3
import csv
products = [
    {"id": 1, "name": "keyboard", "price": 89, "in_stock": True},
    {"id": 2, "name": "monitor", "price": 499, "in_stock": False},
    {"id": 3, "name": "mouse", "price": 35, "in_stock": True},
]
fieldnames=["id","name","price","in_stock"]
with open("products.csv", "w", encoding="utf-8", newline="") as file:
    writer=csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(products)
with open("products.csv", "r", encoding="utf-8", newline="") as file:
    reader=csv.DictReader(file)
    products_loaded=list(reader)
print(products_loaded)
for product in products_loaded:
    product["id"]=int(product["id"])
    product["price"]=int(product["price"])
    normalized = product["in_stock"].strip().lower()
    if normalized == "true":
        product["in_stock"] = True
    elif normalized == "false":
        product["in_stock"] = False
    else:
        raise ValueError(f"Expected true or false, got: {product['in_stock']!r}")

print("Products in stock:")
for product in products_loaded:
    if product["in_stock"]==True:
        print("id:", product["id"], ", name", product["name"], ", price:", product["price"])
#4 
with open("products.json", "w", encoding="utf-8") as file:
    j.dump(products_loaded,file, ensure_ascii=False, indent=2)

with open("products.json", "r", encoding="utf-8") as file:
    products_loaded_json=j.load(file)
a=len(products_loaded_json)
b=0
for product in products_loaded_json:
    if product["price"]==int(product["price"]):
        b+=1
if a==b:
    print("Cisla jsou prevedena spravne")
#4
school = {
    "classes": [
        {
            "name": "1A",
            "students": [
                {"name": "Anna", "grade": 1},
                {"name": "Petr", "grade": 2},
            ],
        },
        {
            "name": "2B",
            "students": [
                {"name": "Eva", "grade": 1},
                {"name": "Marek", "grade": 3},
            ],
        },
    ]
}
with open("school.json", "w", encoding="utf-8") as file:
    j.dump(school, file, ensure_ascii=False, indent=2)
with open("school.json", "r", encoding="utf-8") as file:
    school_loaded=j.load(file)
print(school_loaded)
for cls in school_loaded["classes"]:
    class_name = cls["name"]          # например, "1A", потом "2B"
    students = cls["students"]      # список словарей со студентами этого класса
    student_count = len(students)   # количество студентов
    avg_grade = sum(s["grade"] for s in students) / student_count  # средняя оценка

    print(f"Třída: {class_name}, počet: {student_count}, průměr: {avg_grade:.2f}")





    


    



