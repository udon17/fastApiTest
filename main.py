from fastapi import FastAPI
import logging

# ログの設定
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = FastAPI()

@app.get("/")
def read_root():
    logger.debug("read_root関数が呼び出されました")
    logger.debug("read_root関数が呼び出されました")
    return {"message": "Hello, World!"}