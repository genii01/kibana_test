import logging
import json_logging
import sys
from datetime import datetime


def setup_logging(app):
    # JSON 로깅 초기화
    json_logging.init_fastapi(enable_json=True)
    json_logging.init_request_instrument(app)

    # 루트 로거 설정
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # JSON 포맷 핸들러
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter(
        "{"
        '"@timestamp":"%(asctime)s",'
        '"service":"fastapi",'
        '"container.name":"%(name)s",'
        '"log.level":"%(levelname)s",'
        '"message":"%(message)s",'
        '"event.dataset":"fastapi.application"'
        "}"
    )
    handler.setFormatter(formatter)
    logger.handlers = [handler]

    # FastAPI 앱에 로거 추가
    app.logger = logger
