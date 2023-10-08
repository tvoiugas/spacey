from fastapi import Request

async def log_requests_middleware(request: Request, call_next):
    print(f"Received request: {request.method} {request.url} - {await request.body()}")

    response = await call_next(request)

    return response
    