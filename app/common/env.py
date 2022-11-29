import os
from dotenv import load_dotenv


load_dotenv()

ENV = str(os.environ.get("ENV"))
API_PORT = int(os.environ.get("API_PORT"))

JWT_SECRET_KEY = str(os.environ.get("JWT_SECRET_KEY"))
JWT_ALGORITHM = str(os.environ.get("JWT_ALGORITHM"))

REDIS_URL = str(os.environ.get("REDIS_URL"))
POSTGRESQL_URL = str(os.environ.get("POSTGRESQL_URL"))