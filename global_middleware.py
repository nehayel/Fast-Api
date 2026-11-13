from fastapi import FastAPI,Request

app = FastAPI()

@app.middleware("http")
async def my_middleware(request: Request,call_next):
    print("Middleware: Before Task")

    response = await call_next(request)
    print("Middleware: After Task")

    return response


@app.post("/demo1")
async def demo1():
    return {"demo 1"}


