import os, sys


class BaseConfig(object):
    TYPE = ""
    LOGURU_CONFIG = {}


class DevelopConfig(BaseConfig):
    TYPE = "dev"
    LOGURU_SETTINGS = {
        "handler": [
            dict(sink=sys.stderr, format="{extra[datetime]:%Y-%m-%d %H:%M:%S} | {level.name} | {message}"),
            dict(sink="./log/dev.log", format="{extra[datetime]:%Y-%m-%d %H:%M:%S} | {level.name} | {message}", enqueue=True, serialize=False),
            # dict(sink="./log/dev.log", enqueue=True, serialize=True),
        ],
        "levels": []
    }
    

class ProductionConfig(BaseConfig):
    TYPE = "production"
    LOGURU_SETTINGS = {
        "handler": [
            dict(sink=sys.stderr, format="{extra[datetime]:%Y-%m-%d %H:%M:%S} | {level.name} | {message}"),
            dict(sink="./log/production.log", format="{extra[datetime]:%Y-%m-%d %H:%M:%S} | {level.name} | {message}", enqueue=True, serialize=False),
            # dict(sink="./log/production.log", enqueue=True, serialize=True),
        ],
        "levels": []
    }