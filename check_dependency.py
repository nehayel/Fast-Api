from fastapi import FastAPI, Depends
from MyDependency import check_token, check_admin
app = FastAPI()


@app.get("/huglu", dependencies=[Depends(check_token)])
async def huglu():
    return {"huglu":"fucking Walid"}

@app.get("/huglu_1")
async def huglu_1():
    return {"huglu":"huglu__1"}

@app.get("/huglu_2", dependencies=[Depends(check_token), Depends(check_admin)])
async def huglu_2():
    return {"huglu":"huglu__2"}