import os 
from dotenv import load_dotenv

load_dotenv()

database_infos = {
    "database": os.getenv("URL_DATABASE"),    
}