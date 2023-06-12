import os 
from dotenv import load_dotenv

load_dotenv()

database_infos = {
    "database": os.getenv("DATABASE"),
    "host": os.getenv("HOST"),
    "user": os.getenv("DATABASE_USER"),
    "password": os.getenv("PASSWORD"),
    "port": os.getenv("PORT")
}