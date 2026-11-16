import token

from  fastapi import FastAPI, Request,Header,HTTPException,Depends
app = FastAPI()

# @app.middleware("http") ব্যবহার করে প্রতিটি request এবং response log
@app.middleware("http")
async def middleware(request: Request, call_next):
    print("Request:", request.method, request.url)

    response = await call_next(request)
    print("Request Status:", response.status_code)
    return response

@app.get("/demo")
async def demo():
    return {"this is a middleware test"}



# app.add_middleware দিয়ে class-based middleware
from class_middleware import LoggingMiddleware
app.add_middleware(LoggingMiddleware)
@app.get("/middleware")
async def middleware():
    return "Logging Middleware"



# Header থেকে token গ্রহণ করার dependency
def token_verify(token:str=Header(...)):
    if token != "my_secret_token":
        raise HTTPException(status_code=401,detail="Token vull ache ")
    return token
@app.get("/login", dependencies=[Depends(token_verify)])
async def login():
    return {"Token Verified"}


# একটি token protected route
@app.get("/protected")
async def protected(token:str=Depends(token_verify)):
    return {
        "message":"You are Authenticated",
        "token":token
    }


# admin header check করার dependency
def admin_verify(admin:str=Header(...)):
    if admin != "admin":
        raise HTTPException(status_code=403,detail="Admin Access Required")
    return admin

@app.get("/admin", dependencies=[Depends(admin_verify)])
async def admin() :
    return {"message":"Welcome Admin"}


# token এবং admin header বাধ্যতামূলক করে একটি admin route
def check_admin(admin:str=Header(...)):
    if admin != "admin":
        raise HTTPException(status_code=403,detail="Admin Access Required")
    return admin
def check_token(token:str=Header(...)):
    if token != "walid123":
        raise HTTPException(status_code=401,detail="Invalid Token")
    return token

@app.get("/admin_token", dependencies=[Depends(check_admin), Depends(check_token)])
async def admin_token(token:str=Depends(check_token), admin:str=Depends(check_admin)):
    return {
        "message":"Welcome Admin",
        "token":token,
        "admin":admin
    }