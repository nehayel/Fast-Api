from fastapi import FastAPI, Response, HTTPException
from fastapi.responses import PlainTextResponse, HTMLResponse, JSONResponse
app = FastAPI()

@app.get("/string")
async def string():
    return "Hello Welcome To FastAPI"

@app.get("/number")
async def number():
    return 200

@app.get("/boolean")
async def boolean():
    return True

@app.get("/list")
async def list():
    return ["Python", "FastApi", "Web Scrapping", "DataBase" ]

@app.get("/nested")
async def nested():
    return {
        "name": "Walid Hossain",
        "age": 26,
        "is_active": True,
        "skills": {
            "Backend": ["python", "FastAPI"],
            "Database": ["PostgreSQL", "MySQL", "Redis"]
        }
    }

@app.get("/plain_text")
async def plain_text():
    return  PlainTextResponse(
        content="This is plain text from PlainTextResponse",
    )

@app.get("/html_response")
async def html_response():
    html_content = """
    <html>
        <head>
            <title>FastAPI Assignment </title>
        </head>
        <body>
            <h1>Welcome to FastAPI 3</h1>
            <p>This is an HTML Response</p>
        </body>
    </html>
    """
    return HTMLResponse( content=html_content)

@app.get("/json_response")
async def json_response():
    return JSONResponse(
        status_code=201,
        content={
            "message": "json response",
            "status": 201
        }
    )

@app.get("/http_exception")
async def http_exception():
    raise HTTPException(
        status_code=404,
        detail="Data Not Found",
    )

@app.get("/custom_header")
async def custom_header(response: Response):
    response.headers["Backend"] = "Python FastAPI"
    response.headers["Database"] = "PostgreSQL"

    return {
        "Message": "Custom Header Added",
    }

@app.get("/set_cookie")
async def set_cookie(response: Response):
    response.set_cookie(
        key="Username",
        value="Walid_Hossain",
        httponly=True
    )
    return {
        "Message": "Cookie Added",
    }