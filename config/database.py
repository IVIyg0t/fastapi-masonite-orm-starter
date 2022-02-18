from masoniteorm.connections import ConnectionResolver
from dotenv import load_dotenv
import os
import logging

load_dotenv()

DATABASES = dict(
    default="postgres",
    postgres=dict(
        host="localhost",
        driver="postgres",
        database=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        port=os.getenv("POSTGRES_PORT"),
        log_queries=os.getenv("LOG_QUERIES"),
    ),
)

logger = logging.getLogger("masoniteorm.connection.queries")
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
logger.addHandler(handler)

DB = ConnectionResolver().set_connection_details(DATABASES)
