from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="Talabalar REST API",
    description="REST API bo‘yicha amaliy mashg‘ulot uchun sodda loyiha",
    version="1.0.0"
)

class StudentCreate(BaseModel):
    name: str
    group: str

class Student(StudentCreate):
    id: int

students = [
    {"id": 1, "name": "Ali Valiyev", "group": "1-1"},
    {"id": 2, "name": "Madina Karimova", "group": "1-2"},
]

@app.get("/")
def home():
    return {
        "message": "REST API ishlayapti",
        "swagger": "/docs"
    }

@app.get("/students", response_model=List[Student])
def get_students():
    return students

@app.get("/students/{student_id}", response_model=Student)
def get_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            return student
    raise HTTPException(status_code=404, detail="Talaba topilmadi")

@app.post("/students", response_model=Student, status_code=201)
def create_student(student: StudentCreate):
    new_id = max([s["id"] for s in students], default=0) + 1
    new_student = {
        "id": new_id,
        "name": student.name,
        "group": student.group
    }
    students.append(new_student)
    return new_student

@app.put("/students/{student_id}", response_model=Student)
def update_student(student_id: int, student: StudentCreate):
    for item in students:
        if item["id"] == student_id:
            item["name"] = student.name
            item["group"] = student.group
            return item
    raise HTTPException(status_code=404, detail="Talaba topilmadi")

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    for index, student in enumerate(students):
        if student["id"] == student_id:
            deleted = students.pop(index)
            return {
                "message": "Talaba o‘chirildi",
                "student": deleted
            }
    raise HTTPException(status_code=404, detail="Talaba topilmadi")
