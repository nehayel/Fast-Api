from fastapi import Request
from  starlette.middleware.base import BaseHTTPMiddleware

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        print("Class Middleware: Before Task")

        response = await call_next(request)
        print("Class Middleware: After Task")
        return response