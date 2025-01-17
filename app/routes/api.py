from fastapi import APIRouter, HTTPException, Request
import logging

router = APIRouter()
logger = logging.getLogger(__name__)


@router.get("/hello")
async def hello(request: Request):
    request.app.logger.info("Hello endpoint called")
    return {"message": "Hello World"}


@router.post("/items")
async def create_item(name: str, request: Request):
    request.app.logger.info(f"Creating item with name: {name}")
    return {"item_name": name}


@router.get("/error")
async def trigger_error(request: Request):
    request.app.logger.error("This is a test error")
    raise HTTPException(status_code=500, detail="Test error occurred")


@router.get("/debug")
async def debug_log(request: Request):
    request.app.logger.debug("This is a debug message")
    return {"message": "Debug log created"}


@router.get("/warning")
async def warning_log(request: Request):
    request.app.logger.warning("This is a warning message")
    return {"message": "Warning log created"}
