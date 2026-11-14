from enum import Enum
from fastapi import FastAPI, Request, Header, Form, File, UploadFile
from  pydantic import BaseModel
import os

app = FastAPI()

# path parameter ব্যবহার করে একটি রুট তৈরি
@app.get("/users/{user_name}")
async def get_user(user_name):
    return {"user_name": user_name}

 # path parameter এ type validation যোগ
@app.get("/item/{item_id}")
async def get_user(item_id: int):
    return {"item_id": item_id}

# নির্দিষ্ট option গ্রহণ করার জন্য Enum সহ একটি path route
class CourseName(str, Enum):
    python = "Python",
    java = "Java",
    react = "React"

@app.get("/courses/{course_name}")
async def get_course(course_name: CourseName):
    return {
        "course_name": course_name,
        "message": "Course Found",
    }

# query parameter ব্যবহার করে search বা pagination রুট তৈরি
@app.get("/search")
async def search_employee(name: str, page:int=1, limit:int=5):
    return {
        "search_name": name,
        "page": page,
        "limit": limit,
    }

 # Pydantic BaseModel ব্যবহার করে JSON body গ্রহণ করার POST রুট তৈরি
class Employee(BaseModel):
    name: str
    age: int
    email: str
    salary: float


@app.post("/employee")
async def employee(employee: Employee):
    return {
        "message": "Employee Add Success",
        "employee_data": employee
    }

# Request object ব্যবহার করে headers বা query params দেখানোর রুট তৈরি
@app.get("/request_info")
async def request_info(request: Request):
    return {
        "method": request.method,
        "url":str(request.url),
        "headers": dict(request.headers),
        "query_params": dict(request.query_params),
    }

# Header ব্যবহার করে authorization বা user-agent গ্রহণ করার রুট তৈরি
@app.get("/user_auth")
async def user_auth(name:str = Header(...)
):
    return {
        "authorization": name,
        "message": "Header Received Successfully",

    }
# Form data গ্রহণ করার জন্য একটি রুট তৈরি করুন
@app.post("/login")
async def login(username:str = Form(...), password:str = Form(...)):
    return {
        "username": username,
        "message": "From Data Recieved",
    }

# UploadFile ব্যবহার করে file upload রুট তৈরি করুন
upload_dir = "Assignments/assignment_4/uploads"

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    os.makedirs(upload_dir, exist_ok=True)
    file_path = f"{upload_dir}/{file.filename}"
    content = await file.read()
    with open(file_path, "wb") as f:
        f.write(content)
    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "size": len(content)
    }