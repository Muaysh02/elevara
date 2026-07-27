from fastapi import FastAPI

from app.core.config import settings
from app.core.logging import logger, setup_logging

setup_logging()

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)


@app.get("/")
def root():
    logger.info("Root endpoint accessed")

    return {
        "application": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "debug": settings.DEBUG,
    }