"""NoLoop backend — FastAPI application entry point.

Mirrors the NestJS bootstrap: permissive CORS (reflect origin + credentials),
NestJS-shaped error bodies, and the same route surface on port 4000.
"""

from __future__ import annotations

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.errors import register_error_handlers
from app.db import engine
from app.routers import (
    admin,
    auth,
    beds,
    catalog,
    claims,
    health,
    metrics,
    org,
    track,
)


@asynccontextmanager
async def lifespan(_: FastAPI):
    yield
    await engine.dispose()


app = FastAPI(title="NoLoop backend", version="0.0.1", lifespan=lifespan)

# Allow the web + admin frontends (different origins) to call the API with
# credentials. `allow_origin_regex=".*"` reflects the request origin, matching
# NestJS `enableCors({ origin: true, credentials: true })`.
app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=".*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

register_error_handlers(app)

for module in (auth, admin, org, claims, track, beds, metrics, catalog, health):
    app.include_router(module.router)
