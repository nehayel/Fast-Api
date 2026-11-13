from fastapi import FastAPI
app = FastAPI()
from class_middleware import Mymiddleware



@app.get("/huglu")
async def huglu():
    return {"huglu":"fucking Walid"}

app.add_middleware(Mymiddleware)

@app.get("/huglu_1")
async def huglu_1():
    return {"huglu":"huglu__1"}

@app.get("/huglu_2")
async def huglu_3():
    return {"huglu":"huglu__2"}