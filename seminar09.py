#2
import json
students = [
    {"name": "Anna", "score": 92, "passed": True},
    {"name": "Petr", "score": 71, "passed": True},
    {"name": "Eva", "score": 70, "passed": False},
]

with open("students.json", "w", encoding="utf-8") as file:
    json.dump(students, file, ensure_ascii=False, indent=2)

with open("students.json", "r", encoding="utf-8") as file:
    students=json.load(file)
    #print(students)
for student in students:
    print (student["name"], student["score"])

#3
books={"name": "American Hagwon", "author": "Min Jin Lee", "raite": "99"}
json_books=json.dumps(books, ensure_ascii=False)
print(json_books)

books_text=json.loads(json_books)
print(books_text["name"])


#4
import csv
students=[
    {"name": "Anna", "score": 92, "passed": True},
    {"name": "Petr", "score": 71, "passed": True},
    {"name": "Eva", "score": 70, "passed": False},
]

fieldnames=["name", "score","passed"]
with open ("students.csv", "w", encoding="utf-8", newline="" ) as file:
    writer=csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(students)
with open ("students.csv", "r", encoding="utf-8",newline="" ) as file:
    reader=csv.DictReader(file)
    students_loaded=list(reader)
print(students_loaded)



#5
with open ("students.csv", "r", encoding="utf-8",newline="" ) as file:
    reader=csv.DictReader(file)
    students_loaded=list(reader)
print(students_loaded)
for student in students_loaded:
    student["score"] = int(student["score"])
    student["passed"] = student["passed"] == "True"
b=0
c=0
for student in students_loaded:
    a=int(student["score"])
    b+=a
    c+=1
prumer=b/c
names=[]
for student in students_loaded:
    if student["score"]>49:
        names.append(student["name"])
with open("students1.json", "w", encoding="utf-8") as file:
    json.dump(students,file, ensure_ascii=False, indent=2)
with open("students1.json", "a", encoding="utf-8") as file:
    json.dump(prumer,file, ensure_ascii=False, indent=2)
with open("students1.json", "a", encoding="utf-8") as file:
    json.dump(names,file, ensure_ascii=False, indent=2)

#4
course = {
    "name": "Programování",
    "teacher": "Dr. Novák",
    "students": [
        {"name": "Anna", "score": 92},
        {"name": "Petr", "score": 71},
    ],
}
with open("course.json", "w", encoding="utf-8") as file:
    json.dump(course, file, ensure_ascii=False, indent=2)





 
