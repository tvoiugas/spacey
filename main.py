# System Pathing
import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(BASE_DIR))

# FastAPI
from fastapi import FastAPI, HTTPException, Body
from fastapi.staticfiles import StaticFiles

# Tortoise ORM
from tortoise.contrib.fastapi import register_tortoise

# Local
from constants import db_name
from posts.models import Post, Comment
from description import description
from posts.routes import post_router
from middleware import log_requests_middleware

app = FastAPI(
    title="Space Y",
    description=description,
    swagger_ui_parameters={"defaultModelsExpandDepth": -1},
)

@app.on_event("startup")
async def startup() -> None:
    try:
        redis = Redis(host="localhost", port=6379, db=0)
        app.state.redis = redis
        yield
    finally:
        redis.close()
        redis.connection_pool.disconnect()

app.middleware("http")(log_requests_middleware)

database_url = os.getenv("DB_NAME")

register_tortoise(
    app,
    db_url=f"sqlite://{db_name}.db",
    modules={"models": ["posts.models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)

app.include_router(post_router)

if __name__ == "__main__":
	import uvicorn
	uvicorn.run(app, host="0.0.0.0", port = 8000)
