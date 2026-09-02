from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
async def home():
    return {"message": "This is my first FastAPI assignment"}


@app.get("/greet/{name}")
async def greet(name: str):
    return {"message": f"Hello, {name}!"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)