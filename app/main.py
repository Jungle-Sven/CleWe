from fastapi import FastAPI
from app.core.config import settings
from starlette.middleware.cors import CORSMiddleware

app = FastAPI(
    title='CleWe',
    docs_url=f"{settings.API_PATH}/docs",
    redoc_url=f"{settings.API_PATH}/redoc",
    openapi_url=f"{settings.API_PATH}/openapi.json",
)

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )



@app.get("/")
async def root():
    return {"message": "Hello World"}
