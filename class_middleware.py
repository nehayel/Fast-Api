from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

class Mymiddleware(BaseHTTPMiddleware):
    async def dispatch(self,request: Request,call_next):
        print("Middleware: Before Task From Class Middleware")
        response = await call_next(request)
        print("Middleware: After Task ")
        return response