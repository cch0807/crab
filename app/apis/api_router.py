from fastapi import APIRouter

from app.apis.health import endpoint


api_router = APIRouter()

api_router.include_router(endpoint.router, prefix="/healthz", tags=["healthz"])
