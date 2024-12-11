import csv
from cs50 import SQL

def create_house(house, houses, head):
    count = 0
    for h in houses:
        if h["house"] == house:
            count += 1
    if count == 0:
        houses.append({"house": house, "head": head})


def create_students(name, students):
    students.append({"student_name": name})


def create_assignments(name, house, assignments):
    assignments.append({"student_name": name, "house": house})


db = SQL("sqlite:///roster.db")


students = []
houses = []
assignments = []

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        id = row["id"]
        name = row["student_name"]
        house = row["house"]
        head = row["head"]

        create_house(house, houses, head)
        create_students(name, students)
        create_assignments(name, house, assignments)


for student in students:
    db.execute("INSERT INTO new_students (student_name) VALUES (?)", student["student_name"])

for house in houses:
    db.execute("INSERT INTO houses (house, head) VALUES (?,?)", house["house"], house["head"])

for assignment in assignments:
    db.execute("INSERT INTO assignments (student_name, house) VALUES (?,?)", assignment["student_name"], assignment["house"])
