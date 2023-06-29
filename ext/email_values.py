import os 
from dotenv import load_dotenv

load_dotenv()

email_infos = {
    "email": os.getenv("EMAIL"),
    "password":os.getenv("PASSWORD")    
}