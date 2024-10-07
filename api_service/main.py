from fastapi import FastAPI, Request
from app.gateway_service import route_request_to_service

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "API Gateway"}

@app.api_route("/{full_path:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def proxy(full_path: str, request: Request):
    response = await route_request_to_service(request, full_path)
    return response
