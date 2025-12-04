import os
from dotenv import load_dotenv
import redis

load_dotenv()
REDIS_URL = os.getenv("REDIS_URL")

r=redis.Redis.from_url(REDIS_URL, decode_responses=True)

QR_ID= "Calender_2026"

BASE_URL= os.getenv("BASE_URL")
QR_ENDPOINT =f"{BASE_URL}/qr?id={QR_ID}"

ADMIN_SECRET = os.getenv("ADMIN_SECRET")