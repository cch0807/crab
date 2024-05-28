from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware

from app.apis.api_router import api_router
from app.core.config import get_settings


@asynccontextmanager
async def crab_lifespan(app: FastAPI):
    print("init lifespan")
    yield
    print("clean up lifespan")


app = FastAPI(
    title="crab",
    version="0.0.1",
    description="Crab is information collector",
    docs_url="/",
    lifespan=crab_lifespan,
)

app.include_router(api_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        str(origin) for origin in get_settings().security.backend_cors_origins
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(
    TrustedHostMiddleware, allowed_hosts=get_settings().security.allowed_hosts
)
