from fastapi import FastAPI
app = FastAPI()
@app.get("/demo1")
async def get():
    return {"GET": "it's e get   "}

@app.post("/demo2")
async def post():
    return {"POST": "POST POST"}

@app.put("/demo3")
async def put():
    return {"PUT": "PUT"}

@app.patch("/demo4")
async def patch():
    return {"PATCH": "PATCH"}

@app.delete("/demo5")
async def delete():
    return {"DELETE": "DELETE"}