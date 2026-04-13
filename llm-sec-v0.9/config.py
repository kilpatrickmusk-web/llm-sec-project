#配置文件

import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key")
    DEBUG = os.getenv("FLASK_DEBUG", True)
    # LLM 配置
    LLM_MODEL = "qwen-turbo"
    LLM_TEMPERATURE = 0.9