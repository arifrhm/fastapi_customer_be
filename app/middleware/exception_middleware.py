from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from app.logging_util import log_error


class ExceptionMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            response = await call_next(request)
            return response
        except Exception as e:
            log_error(f"Unhandled error: {str(e)}")
            return JSONResponse(
                status_code=500,
                content={"detail": "Internal Server Error"},
            )
