from fastapi import Header, HTTPException

async def check_token(token:str=Header(...)):
    if token != "abc123":
        raise HTTPException(status_code=401, detail="Vull Token")


async def check_admin(admin:str=Header(...)):
    if admin != "yes":
        raise HTTPException(status_code=401, detail="Only Admin Allow")