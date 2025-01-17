from fastapi import FastAPI
from app.routes import api
from app.logging_config import setup_logging

# FastAPI 앱 인스턴스 생성
app = FastAPI(title="FastAPI Logger Example")

# 로깅 설정
setup_logging(app)

# 라우터 등록
app.include_router(api.router, prefix="/api")


@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI Logger Example"}


@app.on_event("startup")
async def startup_event():
    app.logger.info("Application startup")


@app.on_event("shutdown")
async def shutdown_event():
    app.logger.info("Application shutdown")
