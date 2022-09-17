import os
from dotenv import load_dotenv

load_dotenv()


# api
ENV = str(os.environ.get("ENV"))
API_PORT = int(os.environ.get("API_PORT"))

# gcp
GCS_KEY_FILE = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + str(os.environ.get("GCS_KEY_FILE"))