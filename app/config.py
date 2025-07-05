import os
from dotenv import load_dotenv

load_dotenv()

PORT = int(os.getenv("PORT", 3015))
MONGODB_URI = os.getenv("MONGODB_URI")
MONGODB_DB = os.getenv("MONGODB_DB")
JWT_SECRET = os.getenv("JWT_SECRET")
