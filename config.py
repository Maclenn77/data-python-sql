import os
from dotenv import load_dotenv

load_dotenv()

DB_NAME = os.getenv("DATABASE", default="postgres")
DB_USER = os.getenv("USER", default="postgres")
DB_PASSWORD = os.getenv("PASSWORD", default="postgres")
DB_HOST = os.getenv("HOSTNAME", default="localhost")
DB_PORT = os.getenv("PORT", default="5432")